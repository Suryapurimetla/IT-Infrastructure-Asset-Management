from datetime import timedelta

from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import AllocationRecord, Asset, MaintenanceRecord


def dashboard(request):
    query = request.GET.get('q', '').strip()
    assets = Asset.objects.all()

    if query:
        assets = assets.filter(
            Q(asset_id__icontains=query)
            | Q(name__icontains=query)
            | Q(brand__icontains=query)
        )

    assets = assets.order_by('-created_at')

    today = timezone.localdate()
    expiry_limit = today + timedelta(days=30)
    expiring_assets = Asset.objects.filter(
        warranty_expiry__gte=today,
        warranty_expiry__lte=expiry_limit,
    ).order_by('warranty_expiry')

    for asset in assets:
        if not asset.warranty_expiry:
            asset.warranty_status = 'No Warranty Date'
            asset.days_remaining = None
        elif asset.warranty_expiry < today:
            asset.warranty_status = 'Expired'
            asset.days_remaining = None
        elif asset.warranty_expiry <= expiry_limit:
            asset.warranty_status = 'Expiring Soon'
            asset.days_remaining = (asset.warranty_expiry - today).days
        else:
            asset.warranty_status = 'Active'
            asset.days_remaining = None

    for asset in expiring_assets:
        asset.days_remaining = (asset.warranty_expiry - today).days

    context = {
        'assets': assets,
        'query': query,
        'total_assets': Asset.objects.count(),
        'available_assets': Asset.objects.filter(status='Available').count(),
        'allocated_assets': Asset.objects.filter(status='Allocated').count(),
        'maintenance_assets': Asset.objects.filter(
            status='Under Maintenance'
        ).count(),
        'active_warranties': Asset.objects.filter(
            warranty_expiry__gt=expiry_limit
        ).count(),
        'expiring_warranties': expiring_assets.count(),
        'expired_warranties': Asset.objects.filter(
            warranty_expiry__lt=today
        ).count(),
        'no_warranty_date': Asset.objects.filter(
            warranty_expiry__isnull=True
        ).count(),
        'expiring_assets': expiring_assets,
    }
    return render(request, 'assets/dashboard.html', context)


def add_asset(request):
    if request.method == 'POST':
        asset_id = request.POST.get('asset_id', '').strip()
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', '')
        brand = request.POST.get('brand', '').strip()
        model_number = request.POST.get('model_number', '').strip()
        serial_number = request.POST.get('serial_number', '').strip()
        purchase_date = request.POST.get('purchase_date') or None
        warranty_expiry = request.POST.get('warranty_expiry') or None
        status = request.POST.get('status', 'Available')
        allocated_to = request.POST.get('allocated_to', '').strip()

        if not asset_id or not name:
            return render(request, 'assets/add_asset.html', {
                'error': 'Asset ID and Name are required.',
                'form_data': request.POST,
            })
        if category not in dict(Asset.CATEGORY_CHOICES):
            return render(request, 'assets/add_asset.html', {
                'error': 'Please select a valid category.',
                'form_data': request.POST,
            })
        if status not in dict(Asset.STATUS_CHOICES):
            return render(request, 'assets/add_asset.html', {
                'error': 'Please select a valid status.',
                'form_data': request.POST,
            })
        if Asset.objects.filter(asset_id=asset_id).exists():
            return render(request, 'assets/add_asset.html', {
                'error': 'That Asset ID already exists.',
                'form_data': request.POST,
            })

        Asset.objects.create(
            asset_id=asset_id,
            name=name,
            category=category,
            brand=brand,
            model_number=model_number,
            serial_number=serial_number,
            purchase_date=purchase_date,
            warranty_expiry=warranty_expiry,
            status=status,
            allocated_to=allocated_to,
        )
        return redirect('dashboard')

    return render(request, 'assets/add_asset.html')


def edit_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        new_asset_id = request.POST.get('asset_id', '').strip()
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', '')
        status = request.POST.get('status', 'Available')

        if not new_asset_id or not name:
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Asset ID and Name are required.',
                'form_data': request.POST,
            })
        if category not in dict(Asset.CATEGORY_CHOICES):
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Please select a valid category.',
                'form_data': request.POST,
            })
        if status not in dict(Asset.STATUS_CHOICES):
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Please select a valid status.',
                'form_data': request.POST,
            })
        if Asset.objects.filter(asset_id=new_asset_id).exclude(
            id=asset.id
        ).exists():
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'That Asset ID is already in use.',
                'form_data': request.POST,
            })

        asset.asset_id = new_asset_id
        asset.name = name
        asset.category = category
        asset.brand = request.POST.get('brand', '').strip()
        asset.model_number = request.POST.get('model_number', '').strip()
        asset.serial_number = request.POST.get('serial_number', '').strip()
        asset.purchase_date = request.POST.get('purchase_date') or None
        asset.warranty_expiry = request.POST.get('warranty_expiry') or None
        asset.status = status
        asset.allocated_to = request.POST.get('allocated_to', '').strip()
        asset.save()
        return redirect('dashboard')

    return render(request, 'assets/edit_asset.html', {'asset': asset})


def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('dashboard')
    return render(request, 'assets/delete_asset.html', {'asset': asset})


def allocate_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if asset.status != 'Available':
        return render(request, 'assets/allocate_asset.html', {
            'asset': asset,
            'error': (
                f'This asset cannot be allocated because its '
                f'current status is {asset.status}. '
                f'Only available assets can be allocated.'
            ),
        })

    if request.method == 'POST':
        allocated_to = request.POST.get('allocated_to', '').strip()
        if not allocated_to:
            return render(request, 'assets/allocate_asset.html', {
                'asset': asset,
                'error': 'Please enter the employee name.',
            })

        AllocationRecord.objects.create(
            asset=asset,
            employee_name=allocated_to,
        )
        asset.allocated_to = allocated_to
        asset.status = 'Allocated'
        asset.save()
        return redirect('dashboard')

    return render(request, 'assets/allocate_asset.html', {'asset': asset})


def allocation_history(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    records = asset.allocation_records.order_by('-allocated_at')
    return render(request, 'assets/allocation_history.html', {
        'asset': asset,
        'records': records,
    })


def return_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST' and asset.status == 'Allocated':
        allocation = asset.allocation_records.filter(
            returned_at__isnull=True
        ).order_by('-allocated_at').first()
        if allocation:
            allocation.returned_at = timezone.now()
            allocation.save()
            asset.status = 'Available'
            asset.allocated_to = ''
            asset.save()
    return redirect('dashboard')


def maintain_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status', '')

        if not description:
            return render(request, 'assets/maintenance.html', {
                'asset': asset,
                'error': 'Please enter maintenance details.',
                'description': description,
            })
        if status not in ['Under Maintenance', 'Available']:
            return render(request, 'assets/maintenance.html', {
                'asset': asset,
                'error': 'Please select a valid status.',
                'description': description,
            })

        previous_status = asset.status
        # Keep the maintenance record and asset update atomic.
        with transaction.atomic():
            MaintenanceRecord.objects.create(
                asset=asset,
                description=description,
                previous_status=previous_status,
                new_status=status,
            )
            asset.status = status
            asset.save(update_fields=['status'])

        return redirect('dashboard')

    return render(request, 'assets/maintenance.html', {'asset': asset})


def maintenance_history(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    records = asset.maintenance_records.order_by('-maintenance_date')
    paginator = Paginator(records, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'assets/maintenance_history.html', {
        'asset': asset,
        'records': page_obj,
        'page_obj': page_obj,
    })
