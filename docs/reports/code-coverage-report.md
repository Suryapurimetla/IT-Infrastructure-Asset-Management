# Code Coverage Report

## Project
IT Infrastructure and Asset Management System
Team 08

## Execution Details
- Date: 05 November 2026
- Branch: main
- Commit: 07aa1fd
- Coverage Tool: Coverage.py 7.17.2
- Python: 3.12.10
- Django: 5.2.18

## Test Command
`python -m coverage erase`
`python -m coverage run manage.py test`
`python -m coverage report -m`

## Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 201 |
| Covered statements | 140 |
| Missing statements | 61 |
| Statement coverage | 69.65% |
| Tests executed | 5 |
| Tests passed | 5 |
| Tests failed | 0 |

## File-wise Coverage

| File | Coverage |
|---|---:|
| assets/models.py | 94% |
| assets/views.py | 38% |
| assets/tests.py | 100% |
| assets/admin.py | 100% |
| config/settings.py | 100% |
| config/urls.py | 100% |

## Observations

The overall statement coverage is approximately 70%.

The assets/views.py module has comparatively low coverage because several application workflows, including dashboard, asset registration, editing and deletion, are not exercised by the current automated tests.

## Limitations

This report reflects the five automated tests executed on 05 November 2026. It does not establish that all functional requirements have been tested.

## Conclusion

All five automated tests passed. Additional test cases are required to improve coverage of the application's views and workflows.
