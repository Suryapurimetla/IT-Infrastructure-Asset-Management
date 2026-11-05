# Code Coverage Report

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

`coverage run manage.py test assets`

`coverage report`

## Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 324 |
| Covered statements | 284 |
| Missing statements | 40 |
| Statement coverage | 88% |
| Tests executed | 14 |
| Tests passed | 14 |
| Tests failed | 0 |

## File-wise Coverage

| File | Coverage |
|---|---:|
| assets/__init__.py | 100% |
| assets/admin.py | 100% |
| assets/apps.py | 100% |
| assets/models.py | 91% |
| assets/tests.py | 100% |
| assets/urls.py | 100% |
| assets/views.py | 74% |
| config/__init__.py | 100% |
| config/settings.py | 100% |
| config/urls.py | 100% |
| manage.py | 82% |
| Overall | 88% |

## Observations

The overall statement coverage achieved is 88%.

The assets/views.py module has 74% coverage, indicating that some application view statements are not executed by the current automated test suite.

The assets/models.py module has 91% coverage.

The assets/tests.py and assets/urls.py modules have 100% coverage.

Further test cases can be added to exercise the remaining uncovered application code.

## Limitations

This report reflects the 14 automated tests executed on 05 November 2026 against the uncommitted working-tree version.

The report does not establish complete testing of all functional requirements.

## Conclusion

All 14 automated tests passed successfully. The application achieved 88% overall statement coverage. Additional testing can improve coverage of the remaining uncovered statements, particularly in the application views.

## Next Steps

- Perform system validation against the SRS and Test Plan.
- Review uncovered statements.
- Add further automated tests where required.
- Repeat coverage measurement after final changes.
- Update this report after testing the committed version.