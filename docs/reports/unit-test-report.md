# Unit Test Report

## Project
**IT Infrastructure and Asset Management System**  
**Team 08**

## Execution Details
- Execution date: 14 November 2026
- Branch: Not supplied
- Commit: Not supplied
- Django: 5.2.18
- Test database: Django test database
- Coverage.py: 7.17.2 (used for the subsequent coverage run)
- Python version and operating-system details: Not reverified for this run

## Test Command

`python manage.py test assets --verbosity 2`

## Results Summary

| Measure | Result |
|---|---:|
| Tests found | 26 |
| Passed | 26 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Execution time | 0.524 seconds |
| Django system check | No issues |

A separate branch-enabled coverage run also completed successfully:

`coverage run --branch manage.py test assets`

That run found and passed all 26 tests in 0.571 seconds.

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
| Expired warranty status on dashboard | Pass |
| Active warranty status on dashboard | Pass |
| Warranty expiring today | Pass |
| Warranty expiring exactly in 30 days | Pass |
| Edited asset is searchable | Pass |

## System Check

Django system check completed successfully with no issues.

## Conclusion

All 26 automated tests passed in the latest run. No failures, errors, or skipped tests were reported. The test suite covers asset registration and validation, editing and deletion, dashboard search, allocation and return workflows, maintenance history, and warranty status scenarios.

## Scope and Limitations

The automated tests provide evidence for the scenarios listed above. They do not, by themselves, establish complete system validation against every functional and non-functional requirement in the SRS or Test Plan.

The execution branch and commit were not supplied. The Python version and operating-system details were not reverified for this run.

## Coverage Reference

The latest branch-enabled coverage run reported:
- Statement coverage: 403/420 = 95.95%.
- Standalone branch coverage: 41/56 = 73.21%.
- Combined statement-and-branch coverage: 93%.

Refer to the separate Code Coverage Report and Branch Coverage Report for details.

## Next Steps

- Perform or complete system validation against the submitted SRS and Test Plan.
- Review uncovered statements and branches.
- Update this report after testing the final committed version.
