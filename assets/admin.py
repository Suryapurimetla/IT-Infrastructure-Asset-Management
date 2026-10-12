
from django.contrib import admin
from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'asset_id',
        'name',
        'category',
        'brand',
        'status',
        'allocated_to',
        'purchase_date',
        'warranty_expiry',
    )

    search_fields = (
        'asset_id',
        'name',
        'brand',
        'model_number',
        'serial_number',
        'allocated_to',
    )

    list_filter = (
        'category',
        'status',
        'brand',
    )

    ordering = ('asset_id',)

    list_per_page = 20

    readonly_fields = ('created_at',)
