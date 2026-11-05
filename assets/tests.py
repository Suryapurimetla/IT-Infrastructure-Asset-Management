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
        



class AssetManagementTests(TestCase):
    def setUp(self):
        self.asset = Asset.objects.create(
            asset_id="TEST-003",
            name="Searchable Laptop",
            category="Hardware",
            brand="Dell",
            status="Available",
        )

    def test_add_asset_success(self):
        response = self.client.post(
            reverse("add_asset"),
            {
                "asset_id": "TEST-004",
                "name": "New Desktop",
                "category": "Hardware",
                "brand": "HP",
                "status": "Available",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(
            Asset.objects.filter(asset_id="TEST-004").exists()
        )

    def test_add_asset_rejects_missing_required_fields(self):
        response = self.client.post(
            reverse("add_asset"),
            {
                "asset_id": "",
                "name": "",
                "category": "Hardware",
                "status": "Available",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Asset ID and Name are required."
        )
        self.assertEqual(Asset.objects.count(), 1)

    def test_add_asset_rejects_duplicate_asset_id(self):
        response = self.client.post(
            reverse("add_asset"),
            {
                "asset_id": "TEST-003",
                "name": "Duplicate Laptop",
                "category": "Hardware",
                "status": "Available",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "That Asset ID already exists."
        )
        self.assertEqual(Asset.objects.count(), 1)

    def test_add_asset_rejects_invalid_category(self):
        response = self.client.post(
            reverse("add_asset"),
            {
                "asset_id": "TEST-005",
                "name": "Invalid Asset",
                "category": "InvalidCategory",
                "status": "Available",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Please select a valid category."
        )
        self.assertFalse(
            Asset.objects.filter(asset_id="TEST-005").exists()
        )

    def test_edit_asset_success(self):
        response = self.client.post(
            reverse("edit_asset", args=[self.asset.pk]),
            {
                "asset_id": "TEST-003",
                "name": "Updated Laptop",
                "category": "Hardware",
                "status": "Available",
                "brand": "Lenovo",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.name, "Updated Laptop")
        self.assertEqual(self.asset.brand, "Lenovo")

    def test_edit_asset_rejects_duplicate_asset_id(self):
        Asset.objects.create(
            asset_id="TEST-006",
            name="Another Asset",
            category="Hardware",
            status="Available",
        )

        response = self.client.post(
            reverse("edit_asset", args=[self.asset.pk]),
            {
                "asset_id": "TEST-006",
                "name": "Updated Laptop",
                "category": "Hardware",
                "status": "Available",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "That Asset ID is already in use."
        )

        self.asset.refresh_from_db()
        self.assertEqual(self.asset.asset_id, "TEST-003")

    def test_delete_asset_success(self):
        response = self.client.post(
            reverse("delete_asset", args=[self.asset.pk])
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertFalse(
            Asset.objects.filter(pk=self.asset.pk).exists()
        )

    def test_dashboard_search_by_asset_name(self):
        response = self.client.get(
            reverse("dashboard"),
            {"q": "Searchable"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Searchable Laptop")
        self.assertEqual(response.context["query"], "Searchable")
        self.assertEqual(
            list(response.context["assets"]), [self.asset]
        )