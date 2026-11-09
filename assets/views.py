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

        # Create allocation history record
        AllocationRecord.objects.create(
            asset=asset,
            employee_name=allocated_to,
        )

        # Update asset details
        asset.allocated_to = allocated_to
        asset.status = 'Allocated'
        asset.save()

        return redirect('dashboard')

    return render(request, 'assets/allocate_asset.html', {
        'asset': asset,
    })


# ==========================================
# ALLOCATION HISTORY
# ==========================================

def allocation_history(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    records = asset.allocation_records.order_by('-allocated_at')

    return render(request, 'assets/allocation_history.html', {
        'asset': asset,
        'records': records,
    })


# ==========================================
# RETURN ASSET
# ==========================================

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


# ==========================================
# MAINTENANCE
# ==========================================

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

        # Save the maintenance record and asset status together
        # so both changes succeed or fail as one database transaction.
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

    return render(request, 'assets/maintenance.html', {
        'asset': asset,
    })


# ==========================================
# MAINTENANCE HISTORY
# ==========================================

def maintenance_history(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    records = asset.maintenance_records.order_by(
        '-maintenance_date'
    )

    paginator = Paginator(records, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'assets/maintenance_history.html', {
        'asset': asset,
        'records': page_obj,
        'page_obj': page_obj,
    })
