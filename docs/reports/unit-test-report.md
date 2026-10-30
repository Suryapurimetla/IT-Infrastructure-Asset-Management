# Unit Test Report

## Project
IT Infrastructure and Asset Management System  
Team 08

## Report status
Preliminary test run  
Date: 30 October 2026  
Branch: main  
Commit tested: af60472

## Test environment
- Python: 3.12
- Django: 5.2.18
- Database: MySQL
- Test database: test_itam_db

## Test command
`& "$env:TEMP\itam-venv312-1030\Scripts\python.exe" manage.py test --verbosity 2`

## Results summary

| Measure | Result |
|---|---:|
| Tests found | 5 |
| Passed | 5 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |

## Tests executed

| Test | Result |
|---|---|
| Allocate asset updates employee and status | Pass |
| Allocation requires employee name | Pass |
| Maintenance rejects invalid status | Pass |
| Maintenance requires description | Pass |
| Valid maintenance updates asset status | Pass |

## Conclusion
All five automated tests passed. Django reported no system check issues. The test database was created for the run and removed afterward.

## Scope and limitations
This run covers asset allocation and maintenance status validation. It does not cover all project features or the full system validation. Code coverage and branch coverage are not measured in this report.

Update this report after the team completes testing during November 2-6. Include the final test run, commit, counts, and any unresolved failures.