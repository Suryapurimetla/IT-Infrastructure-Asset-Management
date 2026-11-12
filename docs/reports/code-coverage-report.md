# Code Coverage Report

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

## Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 393 |
| Covered statements | 372 |
| Missing statements | 21 |
| Statement coverage | 372/393 = 94.66% |
| Covered branches | 39/56 = 69.64% |
| Combined coverage | 92% |
| Tests executed | 22 |
| Tests passed | 22 |
| Tests failed | 0 |
| Errors | 0 |
| Execution time | 0.843 seconds |
| Django system check | No issues |

## File-wise Coverage

| File | Statements | Missed | Branches | Partial | Coverage |
|---|---:|---:|---:|---:|---:|
| assets/models.py | 32 | 3 | 0 | 0 | 91% |
| assets/tests.py | 148 | 0 | 0 | 0 | 100% |
| assets/views.py | 136 | 14 | 50 | 14 | 85% |
| config/settings.py | 28 | 2 | 4 | 2 | 88% |
| manage.py | 11 | 2 | 2 | 1 | 77% |
| TOTAL | 393 | 21 | 56 | 17 | 92% |

The table reproduces the supplied coverage output, including its TOTAL row. Per-file percentages are from the branch-enabled run; they are not standalone statement coverage. No updated per-file figures were supplied for files omitted from this table.

## Observations

The overall statement coverage achieved is 372/393 = 94.66%. Overall combined statement and branch coverage is 92%.

The assets/views.py module has 85% combined coverage, with 14 missed statements and 14 partial branches in the supplied output.

The assets/models.py module has 91% coverage.

The assets/tests.py module has 100% coverage. The latest supplied output does not include assets/urls.py.

Further test cases can be added to exercise the remaining uncovered application code.

## Limitations

This report reflects the 22 automated tests from the latest Sprint 2 integration testing run, using results supplied by the project team. The execution date and commit were not supplied. No tests were rerun to prepare this report.

The report does not establish complete testing of all functional requirements.

## Conclusion

All 22 automated tests passed successfully. The application achieved 94.66% statement coverage, 69.64% standalone branch coverage, and 92% overall combined coverage. Additional testing can improve coverage of the remaining uncovered statements, particularly in the application views.

## Next Steps

- Perform system validation against the SRS and Test Plan.
- Review uncovered statements.
- Add further automated tests where required.
- Repeat coverage measurement after final changes.
- Update this report after testing the committed version.