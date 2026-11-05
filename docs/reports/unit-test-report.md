# Unit Test Report

## Project
IT Infrastructure and Asset Management System
Team 08

## Report Status
Preliminary test run — working tree version

- Date: 05 November 2026
- Branch: main
- Base commit: 07aa1fd
- Changes tested: Uncommitted working-tree changes

## Test Environment
- Operating System: Windows
- Python: 3.12.10
- Django: 5.2.18
- Database: MySQL
- Test database: test_itam_db

## Test Command
`python manage.py test --verbosity 2`

## Results Summary

| Measure | Result |
|---|---:|
| Tests found | 13 |
| Passed | 13 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |

## Tests Executed

| Test | Result |
|---|---|
| Allocate asset updates employee and status | Pass |
| Allocation requires employee name | Pass |
| Maintenance rejects invalid status | Pass |
| Maintenance requires description | Pass |
| Valid maintenance updates asset status | Pass |
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
All 13 automated tests passed. The test database was created for the test run and removed afterward.

## Scope and Limitations
The tests cover asset allocation, maintenance status validation, asset registration, duplicate validation, editing, deletion and dashboard search.

The test suite does not establish complete system validation against every SRS requirement.

## Coverage Results

- Statement coverage: 95.12%
- Branch coverage: 72.22%
- Combined coverage: 92.20%

## Next Steps
Perform additional system validation, review uncovered branches, and update this report after the final test execution on the committed version.
