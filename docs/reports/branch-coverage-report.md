# Branch Coverage Report

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
`python -m coverage run --branch manage.py test`
`python -m coverage report -m`

## Branch Coverage Results

| Measure | Result |
|---|---:|
| Total statements | 201 |
| Covered statements | 140 |
| Total branches | 36 |
| Covered branches | 10 |
| Missing branches | 26 |
| Statement coverage | 69.65% |
| Branch coverage | 27.78% |
| Combined coverage | 63.29% |
| Tests passed | 5 |
| Tests failed | 0 |

## Observations

The current automated tests cover 10 out of 36 identified branches.

The remaining 26 branches require additional test scenarios to exercise alternative decision outcomes.

The assets/views.py module is a major area requiring additional test coverage.

## Limitations

The results represent the current five-test suite and should not be interpreted as complete application testing.

## Conclusion

All five automated tests passed. Additional tests covering valid and invalid inputs, conditional outcomes and different application workflows are required to improve branch coverage.
