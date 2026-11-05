# Unit Test Report

## Project
**IT Infrastructure and Asset Management System**
**Team 08**

## Report Status
Latest test run — uncommitted working-tree version

- Date: 05 November 2026
- Branch: `feature/maintenance-history`
- Changes tested: Uncommitted working-tree changes

## Test Environment
- Operating System: Windows
- Python: 3.12.10
- Django: 5.2.18
- Database: MySQL
- Test database: Django test database

## Test Command

`python manage.py test assets`

## Results Summary

| Measure | Result |
|---|---:|
| Tests found | 14 |
| Passed | 14 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Execution time | 0.209 seconds |

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

## System Check

Django system check completed successfully with no issues.

## Conclusion

All 14 automated tests passed successfully. No failures or errors were reported. The test database was created for the test execution and destroyed after completion.

## Scope and Limitations

The automated tests cover:
- Asset registration and validation
- Duplicate Asset ID prevention
- Asset editing and deletion
- Dashboard search
- Asset allocation
- Maintenance status updates
- Maintenance history creation

The automated tests do not establish complete system validation against every SRS requirement.

## Coverage Reference

- Statement coverage: 88% (statement-only coverage run).
- Branch-enabled combined coverage: 84%.
- Refer to the separate Code Coverage Report and Branch Coverage Report for details.

## Next Steps

- Perform system validation against the submitted SRS and Test Plan.
- Review uncovered statements and branches.
- Update the report after final testing on the committed version.