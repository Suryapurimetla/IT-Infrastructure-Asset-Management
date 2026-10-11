# 6. Quality attributes & Acceptance tests

- **Performance:** Asset search should return results within the response-time target specified in ITAM-NF-001.
- **Reliability:** Asset records should remain accurate and consistent during create, view, and update operations.
- **Security:** Protected operations should be accessible only to authorized users, where authentication and access control are implemented.
- **Usability:** Users should be able to navigate asset management functions and understand validation messages.
- **Robustness:** Invalid input and application errors should be handled without unintended changes to saved asset records.

## Acceptance tests

- **Asset Registration Test:** Register a valid hardware or software asset and verify that the record is saved and can be retrieved.
- **Asset Search Test:** Search for an existing asset and verify that the correct matching record is displayed.
- **Asset Update Test:** Update an asset record and verify that the saved changes are reflected correctly.
- **Asset Allocation Test:** Allocate an available asset and verify that the allocation details are recorded.
- **License and Warranty Test:** Enter license and warranty expiry dates and verify that the stored information is correct.
- **Maintenance Test:** Record a maintenance activity and verify that it is associated with the correct asset.
- **Performance Test:** Measure asset search response times and check them against ITAM-NF-001.
- **Security Test:** Attempt to access protected functions without the required permissions and verify that access is denied.
- **Input Validation Test:** Submit missing or invalid data and verify that the system displays an appropriate error message.

## Exit criteria for acceptance

All high-priority functional requirements must be implemented and verified. No critical defects should remain open, and the Requirements Traceability Matrix (RTM) must show the testing status of all requirements. Any unimplemented or untested requirements must be documented as limitations.
