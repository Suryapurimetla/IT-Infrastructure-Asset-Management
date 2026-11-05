# IT Infrastructure and Asset Management System
# Test Case Document

**Team:** 08
**Project:** IT Infrastructure and Asset Management System

## 1. Purpose

This document records the test cases used to validate the implemented asset management functionality. Each test case is mapped to its corresponding SRS requirement wherever applicable.

## 2. Test Environment

- Operating System: Windows
- Python: 3.12.10
- Django: 5.2.18
- Database: MySQL

## 3. Test Cases

### TC-ITAM-01: Add Asset with Valid Details

- **SRS Requirement:** ITAM-F-001
- **Execution Type:** Manual
- **Precondition:** Application is running and the asset dashboard is accessible.
- **Steps:**
  1. Open the asset dashboard.
  2. Select Add Asset.
  3. Enter valid asset details.
  4. Submit the form.
- **Expected Result:** The asset should be saved and displayed in the inventory.
- **Actual Result:** Asset was added successfully.
- **Status:** Pass

### TC-ITAM-02: Reject Duplicate Asset ID

- **SRS Requirement:** ITAM-F-002
- **Execution Type:** Manual
- **Precondition:** An asset with the entered ID already exists.
- **Steps:**
  1. Open the Add Asset form.
  2. Enter an existing Asset ID.
  3. Complete the remaining required fields.
  4. Submit the form.
- **Expected Result:** The duplicate Asset ID should be rejected.
- **Actual Result:** The application displayed a duplicate Asset ID error.
- **Status:** Pass

### TC-ITAM-03: Validate Mandatory Asset Name

- **SRS Requirement:** ITAM-F-003
- **Execution Type:** Manual
- **Precondition:** The Add Asset form is accessible.
- **Steps:**
  1. Open the Add Asset form.
  2. Leave Asset Name empty.
  3. Enter the other required details.
  4. Submit the form.
- **Expected Result:** Submission should be prevented when the mandatory field is empty.
- **Actual Result:** Browser required-field validation was displayed.
- **Status:** Pass

### TC-ITAM-04: Search Asset by Name

- **SRS Requirement:** ITAM-F-004
- **Execution Type:** Automated
- **Precondition:** Asset records are available in the test database.
- **Steps:**
  1. Execute the Django automated test `test_dashboard_search_by_asset_name`.
  2. Verify that the search returns the matching asset.
- **Expected Result:** The dashboard should return matching asset records.
- **Actual Result:** The automated search test passed.
- **Status:** Pass

### TC-ITAM-05: Edit Existing Asset

- **SRS Requirement:** ITAM-F-005
- **Execution Type:** Manual
- **Precondition:** A test asset exists in the inventory.
- **Steps:**
  1. Locate the test asset.
  2. Select Edit.
  3. Update the asset details.
  4. Save the changes.
- **Expected Result:** Updated asset details should be saved and displayed.
- **Actual Result:** The test asset was updated successfully.
- **Status:** Pass

### TC-ITAM-16: Delete Existing Asset

- **SRS Requirement:** ITAM-F-016 (proposed addition)
- **Execution Type:** Manual
- **Precondition:** A test asset exists in the inventory.
- **Steps:**
  1. Locate the test asset.
  2. Select Delete.
  3. Confirm deletion if prompted.
- **Expected Result:** The selected test asset should be removed from the inventory.
- **Actual Result:** The test asset was deleted successfully.
- **Status:** Pass

## 4. Test Execution Summary

| Measure | Result |
|---|---:|
| Manual test cases | 5 |
| Automated test cases referenced | 1 |
| Total documented test cases | 6 |
| Passed | 6 |
| Failed | 0 |

## 5. Automated Test Suite Reference

The complete Django automated test suite was executed using:

`python manage.py test assets`

| Measure | Result |
|---|---:|
| Automated tests executed | 14 |
| Passed | 14 |
| Failed | 0 |
| Errors | 0 |

Detailed execution results are available in `docs/reports/unit-test-report.md`.

## 6. Limitations

The documented cases cover asset registration, duplicate ID validation, mandatory field validation, search, editing and deletion.

Other application features require further validation against the complete SRS and Test Plan.

## 7. Test Case Maintenance

Test cases should be reviewed and updated whenever requirements or implemented features change. Additional cases should be added for new functionality, regression testing and defect verification.