# Branch Coverage Report

## Project

**IT Infrastructure and Asset Management System**
**Team 08**

## Execution Details

- Date: 05 November 2026
- Branch: `feature/maintenance-history`
- Commit: Uncommitted working-tree version
- Coverage Tool: Coverage.py 7.17.2
- Python: 3.12.10
- Django: 5.2.18

## Test Command

`coverage erase`

`coverage run --branch manage.py test assets`

`coverage json -o docs/coverage.json`

## Branch Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 324 |
| Covered lines | 284 |
| Missing lines | 40 |
| Statement coverage | 87.65% (88%) |
| Total branches | 52 |
| Covered branches | 31 |
| Missing branches | 21 |
| Partially covered branches | 13 |
| Standalone branch coverage | 59.62% (60%) |
| Combined coverage | 83.78% (84%) |
| Tests executed | 14 |
| Tests passed | 14 |
| Tests failed | 0 |

## Observations

The branch-enabled coverage execution identified 52 branches across the application.

Out of these, 31 branches were covered and 21 branches were missing.

The report also identified 13 partially covered branches, indicating that some alternative decision paths have not been fully exercised.

The application achieved approximately 60% standalone branch coverage and 84% combined statement and branch coverage.

Further testing can improve coverage of alternative conditional paths, particularly in application views.

## Limitations

This report reflects the 14 automated tests executed on 05 November 2026 against the uncommitted working-tree version.

The report does not establish complete branch coverage or complete validation of all application requirements.

## Conclusion

All 14 automated tests passed successfully during branch-enabled coverage execution.

The application achieved 59.62% standalone branch coverage and 83.78% combined coverage.

Additional test scenarios are recommended to exercise the remaining uncovered branches.

## Next Steps

- Review missing and partially covered branches.
- Add automated tests for alternative conditional outcomes.
- Perform system validation against the SRS and Test Plan.
- Repeat branch coverage measurement after additional tests.
- Update this report after testing the committed version.