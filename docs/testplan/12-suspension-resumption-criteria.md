# 12. Suspension and Resumption Criteria

## 12.1 Suspension Criteria

Testing may be suspended when:

1. The application cannot start or is unavailable.
2. A critical defect blocks further testing.
3. The database or test environment is incorrectly configured.
4. Required test data or dependencies are unavailable.
5. Test execution may damage important data or compromise the test environment.

## 12.2 Actions During Suspension

The team will record the reason for suspension, affected test cases, observed defects, and required corrective actions. Previously recorded results will be retained.

## 12.3 Resumption Criteria

Testing may resume when:

1. The blocking issue has been resolved or an acceptable workaround is available.
2. The application and test environment are operational.
3. Required test data and dependencies are available.
4. Basic smoke tests confirm that the application is ready for further testing.

## 12.4 Retesting After Resumption

Previously failed or blocked test cases will be reviewed and executed again where necessary. Regression testing will be performed when changes may affect existing functionality.
