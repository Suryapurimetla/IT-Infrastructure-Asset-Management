from datetime import timedelta

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Asset, MaintenanceRecord, AllocationRecord


def dashboard(request):
    assets = Asset.objects.all()

    total_assets = assets.count()
    available_assets = assets.filter(status='Available').count()
    allocated_assets = assets.filter(status='Allocated').count()
    maintenance_assets = assets.filter(status='Maintenance').count()

    today = timezone.now().date()
    warranty_alerts = assets.filter(
        warranty_expiry__isnull=False,
        warranty_expiry__lte=today + timedelta(days=30),
        warranty_expiry__gte=today
    )

    search_query = request.GET.get('search', '')
    if search_query:
        assets = assets.filter(
            Q(name__icontains=search_query)
            | Q(asset_tag__icontains=search_query)
            | Q(category__icontains=search_query)
            | Q(location__icontains=search_query)
        )

    context = {
        'assets': assets,
        'total_assets': total_assets,
        'available_assets': available_assets,
        'allocated_assets': allocated_assets,
        'maintenance_assets': maintenance_assets,
        'warranty_alerts': warranty_alerts,
        'search_query': search_query,
    }

    return render(request, 'assets/dashboard.html', context)


def add_asset(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        asset_tag = request.POST.get('asset_tag')
        category = request.POST.get('category')
        location = request.POST.get('location')
        purchase_date = request.POST.get('purchase_date') or None
        warranty_expiry = request.POST.get('warranty_expiry') or None
        status = request.POST.get('status', 'Available')

        if not name or not asset_tag:
            return render(request, 'assets/add_asset.html', {
                'error': 'Asset name and asset tag are required.'
            })

        if Asset.objects.filter(asset_tag=asset_tag).exists():
            return render(request, 'assets/add_asset.html', {
                'error': 'An asset with this asset tag already exists.'
            })

        Asset.objects.create(
            name=name,
            asset_tag=asset_tag,
            category=category,
            location=location,
            purchase_date=purchase_date,
            warranty_expiry=warranty_expiry,
            status=status,
        )

        messages.success(request, 'Asset added successfully.')
        return redirect('dashboard')

    return render(request, 'assets/add_asset.html')


def edit_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        asset_tag = request.POST.get('asset_tag')
        category = request.POST.get('category')
        location = request.POST.get('location')
        purchase_date = request.POST.get('purchase_date') or None
        warranty_expiry = request.POST.get('warranty_expiry') or None
        status = request.POST.get('status')

        if not name or not asset_tag:
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Asset name and asset tag are required.'
            })

        if Asset.objects.filter(asset_tag=asset_tag).exclude(id=asset.id).exists():
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Another asset already uses this asset tag.'
            })

        asset.name = name
        asset.asset_tag = asset_tag
        asset.category = category
        asset.location = location
        asset.purchase_date = purchase_date
        asset.warranty_expiry = warranty_expiry

        if status:
            asset.status = status

        asset.save()

        messages.success(request, 'Asset updated successfully.')
        return redirect('dashboard')

    return render(request, 'assets/edit_asset.html', {
        'asset': asset
    })


def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Asset deleted successfully.')
        return redirect('dashboard')

    return render(request, 'assets/delete_asset.html', {
        'asset': asset
    })


def allocate_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        department = request.POST.get('department')
        allocation_date = request.POST.get('allocation_date') or timezone.now().date()

        if not employee_name:
            return render(request, 'assets/allocate_asset.html', {
                'asset': asset,
                'error': 'Employee name is required.'
            })

        if asset.status != 'Available':
            return render(request, 'assets/allocate_asset.html', {
                'asset': asset,
                'error': (
                    f'This asset cannot be allocated because its '
                    f'current status is {asset.status}. '
                    f'Only available assets can be allocated.'
                )
            })

        with transaction.atomic():
            AllocationRecord.objects.create(
                asset=asset,
                employee_name=employee_name,
                department=department,
                allocation_date=allocation_date,
            )

            asset.status = 'Allocated'
            asset.save()

        messages.success(request, 'Asset allocated successfully.')
        return redirect('dashboard')

    return render(request, 'assets/allocate_asset.html', {
        'asset': asset
    })


def allocation_history(request):
    allocations = AllocationRecord.objects.select_related('asset').all().order_by(
        '-allocation_date'
    )

    return render(request, 'assets/allocation_history.html', {
        'allocations': allocations
    })


def return_asset(request, allocation_id):
    allocation = get_object_or_404(AllocationRecord, id=allocation_id)

    if request.method == 'POST':
        with transaction.atomic():
            allocation.return_date = timezone.now().date()
            allocation.save()

            asset = allocation.asset
            asset.status = 'Available'
            asset.save()

        messages.success(request, 'Asset returned successfully.')
        return redirect('allocation_history')

    return render(request, 'assets/return_asset.html', {
        'allocation': allocation
    })


def maintain_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        maintenance_type = request.POST.get('maintenance_type')
        description = request.POST.get('description')
        maintenance_date = request.POST.get('maintenance_date') or timezone.now().date()
        cost = request.POST.get('cost') or 0

        if not maintenance_type:
            return render(request, 'assets/maintain_asset.html', {
                'asset': asset,
                'error': 'Maintenance type is required.'
            })

        with transaction.atomic():
            MaintenanceRecord.objects.create(
                asset=asset,
                maintenance_type=maintenance_type,
                description=description,
                maintenance_date=maintenance_date,
                cost=cost,
            )

            asset.status = 'Maintenance'
            asset.save()

        messages.success(request, 'Maintenance record added successfully.')
        return redirect('dashboard')

    return render(request, 'assets/maintain_asset.html', {
        'asset': asset
    })


def maintenance_history(request):
    records = MaintenanceRecord.objects.select_related('asset').all().order_by(
        '-maintenance_date'
    )

    paginator = Paginator(records, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'assets/maintenance_history.html', {
        'records': page_obj,
        'page_obj': page_obj,
    })
