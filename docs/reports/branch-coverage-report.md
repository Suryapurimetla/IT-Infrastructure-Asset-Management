# Branch Coverage Report

## Project

**IT Infrastructure and Asset Management System**
**Team 08**

## Execution Details

- Date: Not supplied for the latest run
- Branch: Not supplied for the latest run
- Commit: Not supplied for the latest run
- Coverage Tool: Coverage.py 7.17.2 (previously recorded; not reverified for this run)
- Python: 3.12.10 (previously recorded; not reverified for this run)
- Django: 5.2.18 (previously recorded; not reverified for this run)

## Test Command

`coverage erase`

`coverage run --branch manage.py test assets`

`coverage report`

## Branch Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 393 |
| Covered statements | 372 |
| Missing statements | 21 |
| Statement coverage | 372/393 = 94.66% |
| Total branches | 56 |
| Covered branches | 39 |
| Missing branches | 17 |
| Partial (coverage report) | 17 |
| Standalone branch coverage | 39/56 = 69.64% |
| Combined coverage | 92% |
| Tests executed | 22 |
| Tests passed | 22 |
| Tests failed | 0 |
| Errors | 0 |
| Execution time | 0.843 seconds |
| Django system check | No issues |

## Observations

The branch-enabled coverage execution identified 56 branches across the application.

Out of these, 39 branches were covered and 17 branches were missing.

The report also identified 17 partial branches, indicating that some alternative decision paths have not been fully exercised.

The application achieved 69.64% standalone branch coverage and 92% combined statement and branch coverage.

Further testing can improve coverage of alternative conditional paths, particularly in application views.

## Limitations

This report reflects the 22 automated tests from the latest Sprint 2 integration testing run, using results supplied by the project team. The execution date and commit were not supplied. No tests were rerun to prepare this report.

The report does not establish complete branch coverage or complete validation of all application requirements.

## Conclusion

All 22 automated tests passed successfully during branch-enabled coverage execution.

The application achieved 69.64% standalone branch coverage and 92% combined coverage.

Additional test scenarios are recommended to exercise the remaining uncovered branches.

## Next Steps

- Review missing and partially covered branches.
- Add automated tests for alternative conditional outcomes.
- Perform system validation against the SRS and Test Plan.
- Repeat branch coverage measurement after additional tests.
- Update this report after testing the committed version.