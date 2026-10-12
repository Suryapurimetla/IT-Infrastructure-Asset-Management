
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Asset


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

    context = {
        'assets': assets,
        'query': query,
        'total_assets': Asset.objects.count(),
        'available_assets': Asset.objects.filter(
            status='Available'
        ).count(),
        'allocated_assets': Asset.objects.filter(
            status='Allocated'
        ).count(),
        'maintenance_assets': Asset.objects.filter(
            status='Under Maintenance'
        ).count(),
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
                'error': 'That Asset ID already exists. Use a unique ID.',
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
            })

        if category not in dict(Asset.CATEGORY_CHOICES):
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Please select a valid category.',
            })

        if status not in dict(Asset.STATUS_CHOICES):
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'Please select a valid status.',
            })

        duplicate = Asset.objects.filter(
            asset_id=new_asset_id
        ).exclude(id=asset.id).exists()

        if duplicate:
            return render(request, 'assets/edit_asset.html', {
                'asset': asset,
                'error': 'That Asset ID is already in use.',
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

    return render(request, 'assets/edit_asset.html', {
        'asset': asset,
    })


def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        asset.delete()
        return redirect('dashboard')

    return render(request, 'assets/delete_asset.html', {
        'asset': asset,
    })


def allocate_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        allocated_to = request.POST.get('allocated_to', '').strip()

        if not allocated_to:
            return render(request, 'assets/allocate_asset.html', {
                'asset': asset,
                'error': 'Please enter the employee name.',
            })

        asset.allocated_to = allocated_to
        asset.status = 'Allocated'
        asset.save()

        return redirect('dashboard')

    return render(request, 'assets/allocate_asset.html', {
        'asset': asset,
    })


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

        asset.status = status
        asset.save()

        return redirect('dashboard')

    return render(request, 'assets/maintenance.html', {
        'asset': asset,
    })
