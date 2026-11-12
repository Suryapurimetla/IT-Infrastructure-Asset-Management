from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Asset, MaintenanceRecord, AllocationRecord

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


    def test_maintenance_creates_history_record(self):
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

        record = MaintenanceRecord.objects.get(asset=self.asset)

        self.assertEqual(record.description, "Replaced cooling fan")
        self.assertEqual(record.previous_status, "Available")
        self.assertEqual(record.new_status, "Under Maintenance")

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


# ==========================================
# INTEGRATION TESTS - SPRINT 2
# ==========================================


class AssetIntegrationTests(TestCase):

    def setUp(self):
        self.asset = Asset.objects.create(
            asset_id="INT-001",
            name="Integration Test Laptop",
            category="Hardware",
            brand="Dell",
            status="Available",
        )

    def test_added_asset_appears_on_dashboard(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Integration Test Laptop")
        self.assertEqual(response.context["total_assets"], 1)

    def test_allocation_creates_history_and_updates_dashboard(self):
        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "Integration Employee"},
        )

        self.assertRedirects(response, reverse("dashboard"))

        self.asset.refresh_from_db()

        self.assertEqual(self.asset.status, "Allocated")
        self.assertEqual(
            self.asset.allocated_to,
            "Integration Employee"
        )

        record = AllocationRecord.objects.get(asset=self.asset)

        self.assertEqual(
            record.employee_name,
            "Integration Employee"
        )

        dashboard = self.client.get(reverse("dashboard"))

        self.assertEqual(dashboard.context["allocated_assets"], 1)

    def test_return_asset_updates_status_and_history(self):
        AllocationRecord.objects.create(
            asset=self.asset,
            employee_name="Integration Employee",
        )

        self.asset.status = "Allocated"
        self.asset.allocated_to = "Integration Employee"
        self.asset.save()

        response = self.client.post(
            reverse("return_asset", args=[self.asset.pk])
        )

        self.assertRedirects(response, reverse("dashboard"))

        self.asset.refresh_from_db()

        self.assertEqual(self.asset.status, "Available")
        self.assertEqual(self.asset.allocated_to, "")

        record = AllocationRecord.objects.get(asset=self.asset)

        self.assertIsNotNone(record.returned_at)

    def test_allocation_history_displays_records(self):
        AllocationRecord.objects.create(
            asset=self.asset,
            employee_name="History Employee",
        )

        response = self.client.get(
            reverse("allocation_history", args=[self.asset.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "History Employee")

    def test_maintenance_history_displays_records(self):
        MaintenanceRecord.objects.create(
            asset=self.asset,
            description="Integration maintenance",
            previous_status="Available",
            new_status="Under Maintenance",
        )

        response = self.client.get(
            reverse("maintenance_history", args=[self.asset.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Integration maintenance")

    def test_maintenance_updates_dashboard_status(self):
        self.client.post(
            reverse("maintain_asset", args=[self.asset.pk]),
            {
                "description": "Integration testing maintenance",
                "status": "Under Maintenance",
            },
        )

        self.asset.refresh_from_db()

        self.assertEqual(self.asset.status, "Under Maintenance")

        dashboard = self.client.get(reverse("dashboard"))

        self.assertEqual(dashboard.context["maintenance_assets"], 1)

    def test_warranty_expiring_soon_appears_in_dashboard(self):
        self.asset.warranty_expiry = (
            timezone.localdate() + timedelta(days=10)
        )
        self.asset.save()

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Expiring Soon")

        self.assertEqual(response.context["expiring_warranties"], 1)

    def test_edited_asset_is_searchable(self):
        response = self.client.post(
            reverse("edit_asset", args=[self.asset.pk]),
            {
                "asset_id": "INT-001",
                "name": "Updated Integration Laptop",
                "category": "Hardware",
                "status": "Available",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))

        search_response = self.client.get(
            reverse("dashboard"),
            {"q": "Updated Integration Laptop"},
        )

        self.assertEqual(search_response.status_code, 200)
        self.assertContains(
            search_response,
            "Updated Integration Laptop"
        )
