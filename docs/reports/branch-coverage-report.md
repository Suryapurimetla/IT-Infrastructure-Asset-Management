# Branch Coverage Report

## Project
**IT Infrastructure and Asset Management System**  
**Team 08**

## Execution Details
- Execution date: 14 November 2026
- Branch: Not supplied
- Commit: Not supplied
- Coverage tool: Coverage.py 7.17.2
- Django: 5.2.18
- Python version and operating-system details: Not reverified for this run

## Test Commands

`coverage run --branch manage.py test assets`

`coverage report`

## Branch Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 420 |
| Covered statements | 403 |
| Missing statements | 17 |
| Statement coverage | 403/420 = 95.95% |
| Total branches | 56 |
| Covered branches | 41 |
| Missing branches | 15 |
| Partial branches reported | 15 |
| Standalone branch coverage | 41/56 = 73.21% |
| Combined coverage | 93% |
| Tests executed | 26 |
| Tests passed | 26 |
| Tests failed | 0 |
| Errors | 0 |
| Execution time | 0.571 seconds |
| Django system check | No issues |

## Observations

The branch-enabled coverage execution identified 56 branches.

The coverage report recorded 15 partial branches. Based on the report's branch count and partial-branch count, 41 branches were covered, giving standalone branch coverage of 73.21%.

The application achieved 95.95% statement coverage and 93% combined statement-and-branch coverage.

## Limitations

This report reflects the 26 automated tests from the branch-enabled run on 14 November 2026. The execution branch and commit were not supplied.

Branch coverage measures whether decision outcomes were exercised; it does not establish complete validation of all application requirements or all possible input combinations.

## Conclusion

All 26 automated tests passed during branch-enabled coverage execution. The application achieved 73.21% standalone branch coverage and 93% combined coverage.

## Next Steps

- Review the 15 partial branches, particularly in application views.
- Add automated tests for important alternative conditional outcomes where appropriate.
- Perform system validation against the SRS and Test Plan.
- Repeat branch coverage measurement after final changes and on the committed version.
