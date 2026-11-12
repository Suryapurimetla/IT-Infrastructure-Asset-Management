# Unit Test Report

## Project
**IT Infrastructure and Asset Management System**
**Team 08**

## Report Status
Latest test run: Sprint 2 integration testing (results supplied by the project team)

- Date: Not supplied for the latest run
- Branch: Not supplied for the latest run
- Changes tested: Sprint 2 integration testing; commit status not supplied

## Test Environment
- Operating System: Windows (previously recorded; not reverified for this run)
- Python: 3.12.10 (previously recorded; not reverified for this run)
- Django: 5.2.18 (previously recorded; not reverified for this run)
- Database: MySQL
- Test database: Django test database

## Test Command

`coverage erase`

`coverage run --branch manage.py test assets`

`coverage report`

## Results Summary

| Measure | Result |
|---|---:|
| Tests found | 22 |
| Passed | 22 |
| Failed | 0 |
| Errors | 0 |
| Skipped | Not supplied |
| Execution time | 0.843 seconds |

## Tests Executed

| Test | Result |
|---|---|
| Allocate asset updates employee and status | Pass |
| Allocation requires employee name | Pass |
| Maintenance rejects invalid status | Pass |
| Maintenance requires description | Pass |
| Valid maintenance updates asset status | Pass |
| Maintenance creates history record | Pass |
| Add asset successfully | Pass |
| Add asset rejects missing required fields | Pass |
| Add asset rejects duplicate asset ID | Pass |
| Add asset rejects invalid category | Pass |
| Edit asset successfully | Pass |
| Edit asset rejects duplicate asset ID | Pass |
| Delete asset successfully | Pass |
| Dashboard search by asset name | Pass |
| Added asset appears on dashboard | Pass |
| Allocation creates history and updates dashboard | Pass |
| Return asset updates status and history | Pass |
| Allocation history displays records | Pass |
| Maintenance history displays records | Pass |
| Maintenance updates dashboard status | Pass |
| Warranty expiring soon appears in dashboard | Pass |
| Edited asset is searchable | Pass |

## System Check

Django system check completed successfully with no issues.

## Conclusion

All 22 automated tests passed successfully. No failures or errors were reported. Results are supplied by the project team; no tests were rerun to prepare this report.

## Scope and Limitations

The automated tests cover:
- Asset registration and validation
- Duplicate Asset ID prevention
- Asset editing and deletion
- Dashboard search
- Asset allocation
- Maintenance status updates
- Maintenance history creation and display
- Allocation history creation and display
- Asset returns and history updates
- Dashboard status counts and expiring warranty display
- Search after asset editing

The automated tests do not establish complete system validation against every SRS requirement.

## Coverage Reference

- Statement coverage: 372/393 = 94.66% (from the branch-enabled run).
- Standalone branch coverage: 39/56 = 69.64%.
- Branch-enabled combined coverage: 92%.
- Refer to the separate Code Coverage Report and Branch Coverage Report for details.

## Next Steps

- Perform system validation against the submitted SRS and Test Plan.
- Review uncovered statements and branches.
- Update the report after final testing on the committed version.