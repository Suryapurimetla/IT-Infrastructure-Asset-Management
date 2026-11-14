# System Validation Report

## Project
**IT Infrastructure and Asset Management System**  
**Team 08**

## Latest Automated Execution Details
- Execution date: 14 November 2026
- Branch: Not supplied
- Commit: Not supplied
- Django: 5.2.18
- Test database: Django test database
- Python version and operating-system details: Not reverified for this run

## Objective

The objective of system validation is to verify that the IT Infrastructure and Asset Management System performs its major asset management operations correctly and satisfies the expected application behaviour.

## Validation Scope

The project validation scope includes:

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

## Previously Recorded Manual Validation

The following manual validation results were recorded on 05 November 2026. They are retained as historical evidence and were not rerun as part of the 14 November automated test execution.

| Test Scenario | Expected Result | Previously Observed Result | Historical Status |
|---|---|---|---|
| Add asset with valid details | Asset should be saved | Asset added successfully | Pass |
| Add duplicate Asset ID | Duplicate should be rejected | Duplicate ID error displayed | Pass |
| Submit missing mandatory fields | Submission should be prevented | Required-field validation displayed | Pass |
| Edit existing asset | Asset details should update | Asset updated successfully | Pass |
| Delete test asset | Asset should be removed | Test asset deleted successfully | Pass |

## Latest Automated Validation Results

The automated Django test suite was executed using:

`python manage.py test assets --verbosity 2`

| Measure | Result |
|---|---:|
| Tests found | 26 |
| Passed | 26 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Execution time | 0.524 seconds |
| Django system check | No issues |

A separate branch-enabled coverage run also found and passed all 26 tests in 0.571 seconds.

## Automated Scenarios Covered

The 26 tests cover:
- Asset allocation and employee-name validation
- Maintenance status updates, history creation and input validation
- Asset creation, required-field validation, duplicate ID prevention and category validation
- Asset editing, duplicate ID prevention and deletion
- Dashboard display and asset-name search
- Allocation history and asset return
- Maintenance history and dashboard maintenance status
- Warranty expiring soon, expired warranty, active warranty, expiry today and expiry exactly 30 days away
- Search after editing an asset

## Observations

The latest automated run completed with all 26 tests passing and no Django system-check issues.

The automated test suite exercises key asset management, allocation, maintenance, dashboard, history and warranty scenarios.

## Limitations

The manual validation results in this report are historical results from 05 November 2026; they were not repeated on 14 November.

Passing automated tests do not establish that every functional and non-functional requirement has been validated. Full system validation against the complete SRS and Test Plan remains necessary.

The execution branch and commit for the latest automated run were not supplied.

## Conclusion

The latest automated validation run completed successfully: all 26 tests passed, with no failures, errors or skipped tests. The previously recorded manual validation scenarios are retained with their original date and are not represented as newly executed.

The application demonstrated the expected behaviour in the automated scenarios listed in this report. Further requirement-by-requirement validation should be completed before final submission.

## Next Steps

- Validate remaining functional requirements against the SRS and Test Plan.
- Perform and record manual validation for scenarios not covered by automated tests.
- Review identified defects and fix them.
- Repeat system validation on the final committed version.
- Maintain screenshots and test execution evidence.
