# 3.7 Risks & Mitigations

The development of the IT Infrastructure & Asset Management System may involve technical, security, data management, and project-related risks. The following table identifies potential risks and the proposed measures to reduce their impact.

| Risk | Potential Impact | Mitigation Strategy |
|---|---|---|
| Inconsistent Asset Records | Incorrect asset details may lead to inaccurate tracking and allocation decisions. | Apply input validation, use unique asset identifiers, and define appropriate database constraints. |
| Unauthorized Access | Users may access or modify information beyond their permitted responsibilities. | Define appropriate access permissions and implement authentication and authorization controls where required. |
| Invalid User Input | Incorrect or incomplete input may cause errors or unreliable records. | Validate required fields, data formats, and input values before processing requests. |
| Database Failure | Asset information may become unavailable or operations may fail. | Plan database backup and recovery procedures and handle database errors appropriately. |
| Data Loss | Missing records may disrupt asset tracking and maintenance activities. | Establish suitable backup procedures and verify recovery arrangements before deployment. |
| Integration Problems | Components may not exchange information correctly. | Define clear component interfaces and test interactions between the user interface, application logic, and database. |
| Scope Changes | New requirements may increase implementation time and complexity. | Review proposed changes with the team and update the SRS, SAD, and STP when necessary. |
| Schedule Delays | Documentation, implementation, and testing may not be completed on time. | Prioritize core requirements, assign responsibilities, and review progress regularly. |
| Technology Uncertainty | An unsuitable or unfamiliar technology may delay implementation. | Confirm the technology stack early and select tools that the team can use effectively. |
| Incomplete Test Coverage | Defects may remain undetected before submission. | Map requirements to test cases through the RTM and review test coverage against the SRS. |

## Risk Management Approach

The project team should review these risks throughout design, implementation, and testing. If a risk becomes an actual issue, the team should record its impact, assign responsibility for addressing it, and update the relevant project documents where necessary.

The mitigation strategies listed above are planned actions. Their completion should only be recorded after the team has implemented and verified the corresponding measures.
