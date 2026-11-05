# System Validation Report

## Project

**IT Infrastructure and Asset Management System**
**Team 08**

## Execution Details

- Date: 05 November 2026
- Branch: `feature/maintenance-history`
- Version tested: Uncommitted working-tree version
- Operating System: Windows
- Python: 3.12.10
- Django: 5.2.18
- Database: MySQL

## Objective

The objective of system validation is to verify that the IT Infrastructure and Asset Management System performs its major asset management operations correctly and satisfies the expected application behaviour.

## Validation Scope

The following application functionalities were considered:

1. Asset registration
2. Duplicate Asset ID validation
3. Mandatory field validation
4. Asset editing
5. Asset deletion
6. Dashboard and asset inventory
7. Asset allocation
8. Maintenance management
9. Maintenance history
10. Warranty tracking
11. Allocation history
12. Asset return

## Manual Validation Results

| Test Scenario | Expected Result | Observed Result | Status |
|---|---|---|---|
| Add asset with valid details | Asset should be saved | Asset added successfully | Pass |
| Add duplicate Asset ID | Duplicate should be rejected | Duplicate ID error displayed | Pass |
| Submit missing mandatory fields | Submission should be prevented | Required-field validation displayed | Pass |
| Edit existing asset | Asset details should update | Asset updated successfully | Pass |
| Delete test asset | Asset should be removed | Test asset deleted successfully | Pass |

## Automated Validation Results

The Django automated test suite was executed using:

`python manage.py test assets`

| Measure | Result |
|---|---:|
| Tests executed | 14 |
| Passed | 14 |
| Failed | 0 |
| Errors | 0 |
| Django system check | No issues |

## Observations

The manual validation confirmed that asset registration, duplicate ID validation, mandatory field validation, editing and deletion worked as expected during testing.

The automated tests covered asset management, allocation, maintenance and dashboard search functionality.

## Limitations

The manual validation scenarios listed above do not represent exhaustive validation of every system feature or every SRS requirement.

The automated test results represent the uncommitted working-tree version tested on 05 November 2026.

Further system validation is required for all remaining functional and non-functional requirements.

## Conclusion

The tested asset management workflows and all 14 automated Django tests completed successfully.

The application demonstrated the expected behaviour in the tested scenarios. Additional validation should be performed against the complete Software Requirements Specification and Test Plan before final submission.

## Next Steps

- Validate all remaining functional requirements.
- Perform integration and regression testing.
- Review identified defects and fix them.
- Repeat system validation on the final committed version.
- Maintain screenshots and test execution evidence.