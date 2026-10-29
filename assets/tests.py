from django.test import TestCase
from django.urls import reverse

from .models import Asset


class AssetAllocationTests(TestCase):
    def setUp(self):
        self.asset = Asset.objects.create(
            asset_id="TEST-001",
            name="Test Laptop",
            category="Hardware",
            status="Available",
        )

    def test_allocate_asset_updates_employee_and_status(self):
        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "Test Student"},
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.allocated_to, "Test Student")
        self.assertEqual(self.asset.status, "Allocated")

    def test_allocation_requires_employee_name(self):
        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "   "},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter the employee name.")


class AssetMaintenanceTests(TestCase):
    def setUp(self):
        self.asset = Asset.objects.create(
            asset_id="TEST-002",
            name="Test Router",
            category="Network",
            status="Available",
        )

    def test_valid_maintenance_updates_asset_status(self):
        response = self.client.post(
            reverse("maintain_asset", args=[self.asset.pk]),
            {
                "description": "Replaced cooling fan",
                "status": "Under Maintenance",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.status, "Under Maintenance")

    def test_maintenance_requires_description(self):
        response = self.client.post(
            reverse("maintain_asset", args=[self.asset.pk]),
            {"description": "   ", "status": "Under Maintenance"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter maintenance details.")

    def test_maintenance_rejects_invalid_status(self):
        response = self.client.post(
            reverse("maintain_asset", args=[self.asset.pk]),
            {"description": "Inspection", "status": "Retired"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please select a valid status.")