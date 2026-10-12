# 13. Test Case Management and Traceability

## 13.1 Test Case Identification

Each test case will have a unique identifier, such as TC-ITAM-01, TC-ITAM-02, and TC-ITAM-03. These identifiers will be used when recording execution results and reporting defects.

## 13.2 Test Case Records

Each test case should include:

- Test case ID and title.
- Related SRS requirement ID.
- Preconditions and test data.
- Execution steps.
- Expected result.
- Actual result.
- Status: Not Run, Pass, or Fail.
- Remarks or linked defect ID, where applicable.

## 13.3 Requirements Traceability

Test cases will be mapped to the relevant requirements in the SRS. The Requirements Traceability Matrix (RTM) will record requirement IDs, descriptions, related test case IDs, and testing status.

## 13.4 Test Case Maintenance

Test cases will be reviewed and updated when requirements or implemented features change. New test cases will be added when necessary.

## 13.5 Defect Traceability

Failed test cases will be linked to corresponding defect records where possible. After a defect is corrected, the affected test case will be executed again and its status updated based on the actual result.
