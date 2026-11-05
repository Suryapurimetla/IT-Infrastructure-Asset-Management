
from django.db import models


class Asset(models.Model):

    CATEGORY_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Network', 'Network'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Allocated', 'Allocated'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Retired', 'Retired'),
    ]

    asset_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    brand = models.CharField(max_length=100, blank=True)
    model_number = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    warranty_expiry = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Available'
    )
    allocated_to = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset_id} - {self.name}"


class MaintenanceRecord(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='maintenance_records'
    )

    description = models.TextField()
    previous_status = models.CharField(max_length=30)
    new_status = models.CharField(max_length=30)
    maintenance_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.asset_id} - {self.maintenance_date}"



# ==========================================
# ASSET ALLOCATION HISTORY
# ==========================================

class AllocationRecord(models.Model):
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='allocation_records'
    )

    employee_name = models.CharField(max_length=100)

    allocated_at = models.DateTimeField(auto_now_add=True)

    returned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.asset.asset_id} - {self.employee_name}"
