# 3.2 Stakeholders & Concerns

The IT Infrastructure & Asset Management System has several stakeholders. Each stakeholder has different responsibilities and expectations for the system.

| Stakeholder | Responsibilities | Main Concerns |
|---|---|---|
| IT Administrator | Maintains asset records and manages asset information. | Accurate records, efficient asset updates, and easy searching. |
| Asset Manager | Oversees asset allocation, availability, and maintenance activities. | Correct allocation status, asset availability, and maintenance tracking. |
| Authorized User | Views or uses asset information according to assigned permissions. | Ease of use, accurate information, and appropriate access permissions. |
| System Administrator | Manages system configuration and user access, if this role is included in the implementation. | Access control, system reliability, and secure configuration. |
| Developer | Designs, implements, and maintains the application. | Clear component responsibilities, maintainable code, and testability. |
| Test Engineer | Verifies that the system behaves according to its requirements. | Requirement coverage, reproducible test results, and defect identification. |
| Project Evaluator | Reviews the project documentation, design, and implementation. | Requirement completeness, consistency across documents, and evidence of testing. |

### Stakeholder Concerns and Architectural Responses

The architecture is intended to address the stakeholders' concerns as follows:

1. **Accurate asset information:** Asset-related operations should use consistent validation and data-management rules.
2. **Controlled access:** Access to protected functions should be restricted according to the permissions defined for each user role.
3. **Maintainability:** The system should separate major responsibilities into components that can be developed and maintained independently where practical.
4. **Testability:** Components should have clear responsibilities and interfaces so their behaviour can be verified against the SRS and STP.
5. **Usability:** The user interface should make common operations, such as registering, searching, updating, and allocating assets, straightforward.
6. **Traceability:** Design decisions should support the requirements documented in the SRS and be verifiable through the planned testing process.

The stakeholder roles listed above are proposed for the system design. The team should confirm the final user roles and permissions before implementation so that the architecture matches the actual project scope.
