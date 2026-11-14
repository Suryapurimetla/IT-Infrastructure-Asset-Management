# Code Coverage Report

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

`coverage html`

## Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 420 |
| Missed statements | 17 |
| Covered statements | 403 |
| Statement coverage | 403/420 = 95.95% |
| Total branches | 56 |
| Partial branches | 15 |
| Covered branches | 41 |
| Standalone branch coverage | 41/56 = 73.21% |
| Combined statement-and-branch coverage | 93% |
| Tests executed | 26 |
| Tests passed | 26 |
| Tests failed | 0 |
| Errors | 0 |
| Execution time | 0.571 seconds |
| Django system check | No issues |

## File-wise Coverage

| File | Statements | Missed | Branches | Partial | Coverage |
|---|---:|---:|---:|---:|---:|
| assets/models.py | 32 | 3 | 0 | 0 | 91% |
| assets/tests.py | 175 | 0 | 0 | 0 | 100% |
| assets/views.py | 136 | 10 | 50 | 12 | 88% |
| config/settings.py | 28 | 2 | 4 | 2 | 88% |
| manage.py | 11 | 2 | 2 | 1 | 77% |
| TOTAL | 420 | 17 | 56 | 15 | 93% |

Other listed files in the terminal output, including the app configuration, admin module, migrations, URL modules and package initializers, reported 100% coverage.

## Observations

The latest branch-enabled run measured 420 statements and 56 branches. It recorded 17 missed statements and 15 partial branches.

The overall statement coverage is 95.95%. Standalone branch coverage is 73.21%, and combined statement-and-branch coverage is reported as 93%.

The `assets/views.py` module reported 88% combined coverage, with 10 missed statements and 12 partial branches. The `assets/tests.py` module reported 100% coverage.

## Limitations

Coverage indicates which measured statements and branches were exercised by this test run. It does not prove that all requirements, user workflows, or production conditions have been validated.

The execution branch and commit were not supplied. Python version and operating-system details were not reverified for this run.

## Conclusion

All 26 automated tests passed during the branch-enabled coverage run. The application achieved 95.95% statement coverage, 73.21% standalone branch coverage, and 93% combined coverage.

## Next Steps

- Review the remaining missed statements and partial branches, especially in application views.
- Add tests where uncovered paths represent important application behaviour.
- Perform system validation against the SRS and Test Plan.
- Repeat coverage measurement after final changes and on the committed version.
