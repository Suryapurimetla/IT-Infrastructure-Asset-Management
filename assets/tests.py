
from unittest.mock import patch
from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

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

    def test_successful_allocation_creates_history_record(self):
        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "Purvik"},
        )

        self.assertRedirects(response, reverse("dashboard"))

        record = AllocationRecord.objects.get(asset=self.asset)
        self.assertEqual(record.employee_name, "Purvik")
        self.assertIsNone(record.returned_at)

    def test_allocation_rejects_already_allocated_asset(self):
        self.asset.status = "Allocated"
        self.asset.save()

        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "Purvik"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Only available assets can be allocated."
        )

        self.asset.refresh_from_db()
        self.assertEqual(self.asset.status, "Allocated")
        self.assertEqual(AllocationRecord.objects.count(), 0)

    def test_allocation_rejects_retired_asset(self):
        self.asset.status = "Retired"
        self.asset.save()

        response = self.client.post(
            reverse("allocate_asset", args=[self.asset.pk]),
            {"allocated_to": "Purvik"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AllocationRecord.objects.count(), 0)

    def test_allocation_history_displays_records(self):
        AllocationRecord.objects.create(
            asset=self.asset,
            employee_name="Purvik",
        )

        response = self.client.get(
            reverse("allocation_history", args=[self.asset.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Purvik")


class AssetMaintenanceTests(TestCase):
    def setUp(self):
        self.asset = Asset.objects.create(
            asset_id="TEST-002",
            name="Test Router",
            category="Network",
            status="Available",
        )

    def test_maintenance_history_paginates_records(self):
        for i in range(12):
            MaintenanceRecord.objects.create(
                asset=self.asset,
                description=f"Maintenance task {i}",
                previous_status="Available",
                new_status="Under Maintenance",
            )

        response = self.client.get(
            reverse("maintenance_history", args=[self.asset.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["records"]), 10)
        self.assertEqual(response.context["page_obj"].number, 1)
        self.assertTrue(response.context["page_obj"].has_next())

    def test_maintenance_history_second_page(self):
        for i in range(12):
            MaintenanceRecord.objects.create(
                asset=self.asset,
                description=f"Maintenance task {i}",
                previous_status="Available",
                new_status="Under Maintenance",
            )

        response = self.client.get(
            reverse("maintenance_history", args=[self.asset.pk]),
            {"page": 2},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["records"]), 2)
        self.assertEqual(response.context["page_obj"].number, 2)
        self.assertFalse(response.context["page_obj"].has_next())

    def test_maintenance_history_paginates_records_duplicate(self):
        for i in range(12):
            MaintenanceRecord.objects.create(
                asset=self.asset,
                description=f"Maintenance task {i}",
                previous_status="Available",
                new_status="Under Maintenance",
            )

        response = self.client.get(
            reverse("maintenance_history", args=[self.asset.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["records"]), 10)
        self.assertEqual(response.context["page_obj"].number, 1)
        self.assertTrue(response.context["page_obj"].has_next())

    def test_maintenance_history_second_page_duplicate(self):
        for i in range(12):
            MaintenanceRecord.objects.create(
                asset=self.asset,
                description=f"Maintenance task {i}",
                previous_status="Available",
                new_status="Under Maintenance",
            )

        response = self.client.get(
            reverse("maintenance_history", args=[self.asset.pk]),
            {"page": 2},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["records"]), 2)
        self.assertEqual(response.context["page_obj"].number, 2)
        self.assertFalse(response.context["page_obj"].has_next())

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

    def test_maintenance_record_rolls_back_if_asset_update_fails(self):
        with patch.object(
            Asset,
            'save',
            side_effect=RuntimeError('Simulated asset update failure'),
        ):
            with self.assertRaises(RuntimeError):
                self.client.post(
                    reverse("maintain_asset", args=[self.asset.pk]),
                    {
                        "description": "Replaced cooling fan",
                        "status": "Under Maintenance",
                    },
                )

        self.assertEqual(
            MaintenanceRecord.objects.filter(asset=self.asset).count(),
            0,
        )

        self.asset.refresh_from_db()
        self.assertEqual(self.asset.status, "Available")

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
        self.assertContains(response, "Asset ID and Name are required.")
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
        self.assertContains(response, "That Asset ID already exists.")
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
        self.assertContains(response, "Please select a valid category.")
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
        self.assertContains(response, "That Asset ID is already in use.")

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

    def test_dashboard_search_by_asset_id(self):
        response = self.client.get(
            reverse("dashboard"),
            {"q": "TEST-003"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TEST-003")
        self.assertEqual(
            list(response.context["assets"]), [self.asset]
        )

    def test_dashboard_search_by_brand(self):
        response = self.client.get(
            reverse("dashboard"),
            {"q": "Dell"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Searchable Laptop")
        self.assertEqual(
            list(response.context["assets"]), [self.asset]
        )


class DashboardSummaryTests(TestCase):
    def setUp(self):
        today = date.today()

        self.active_asset = Asset.objects.create(
            asset_id="DASH-001",
            name="Active Laptop",
            category="Hardware",
            status="Available",
            warranty_expiry=today + timedelta(days=60),
        )

        self.expiring_asset = Asset.objects.create(
            asset_id="DASH-002",
            name="Expiring Monitor",
            category="Hardware",
            status="Allocated",
            warranty_expiry=today + timedelta(days=10),
        )

        self.expired_asset = Asset.objects.create(
            asset_id="DASH-003",
            name="Expired Desktop",
            category="Hardware",
            status="Under Maintenance",
            warranty_expiry=today - timedelta(days=10),
        )

        self.no_warranty_asset = Asset.objects.create(
            asset_id="DASH-004",
            name="No Warranty Keyboard",
            category="Hardware",
            status="Available",
            warranty_expiry=None,
        )

    def test_dashboard_summary_counts(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["total_assets"], 4)
        self.assertEqual(response.context["available_assets"], 2)
        self.assertEqual(response.context["allocated_assets"], 1)
        self.assertEqual(response.context["maintenance_assets"], 1)

        self.assertEqual(response.context["active_warranties"], 1)
        self.assertEqual(response.context["expiring_warranties"], 1)
        self.assertEqual(response.context["expired_warranties"], 1)
        self.assertEqual(response.context["no_warranty_date"], 1)

    def test_dashboard_displays_correct_warranty_statuses(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

        assets = {
            asset.asset_id: asset
            for asset in response.context["assets"]
        }

        self.assertEqual(
            assets["DASH-001"].warranty_status,
            "Active",
        )

        self.assertEqual(
            assets["DASH-002"].warranty_status,
            "Expiring Soon",
        )

        self.assertEqual(
            assets["DASH-003"].warranty_status,
            "Expired",
        )

        self.assertEqual(
            assets["DASH-004"].warranty_status,
            "No Warranty Date",
        )

    def test_warranty_status_boundary_dates(self):
        today = date.today()

        Asset.objects.create(
            asset_id="BOUNDARY-001",
            name="Warranty Expires Today",
            category="Hardware",
            warranty_expiry=today,
        )

        Asset.objects.create(
            asset_id="BOUNDARY-002",
            name="Warranty Expires in 30 Days",
            category="Hardware",
            warranty_expiry=today + timedelta(days=30),
        )

        Asset.objects.create(
            asset_id="BOUNDARY-003",
            name="Warranty Expires in 31 Days",
            category="Hardware",
            warranty_expiry=today + timedelta(days=31),
        )

        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

        assets = {
            asset.asset_id: asset
            for asset in response.context["assets"]
        }

        self.assertEqual(
            assets["BOUNDARY-001"].warranty_status,
            "Expiring Soon",
        )

        self.assertEqual(
            assets["BOUNDARY-002"].warranty_status,
            "Expiring Soon",
        )

        self.assertEqual(
            assets["BOUNDARY-003"].warranty_status,
            "Active",
        )

    # Issue #26: Warranty Expiry Alerts
    def test_warranty_expiry_alerts_show_only_next_30_days(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

        alert_ids = [
            asset.asset_id
            for asset in response.context["expiring_assets"]
        ]

        self.assertIn("DASH-002", alert_ids)
        self.assertNotIn("DASH-001", alert_ids)
        self.assertNotIn("DASH-003", alert_ids)
        self.assertNotIn("DASH-004", alert_ids)

    def test_warranty_expiry_alert_shows_days_remaining(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

        expiring_asset = next(
            asset
            for asset in response.context["expiring_assets"]
            if asset.asset_id == "DASH-002"
        )

        self.assertEqual(expiring_asset.days_remaining, 10)
