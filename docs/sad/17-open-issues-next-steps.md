# 4.6 Open Issues & Next Steps

## 4.6.1 Open Issues

The following items require confirmation or further work before the architecture and design can be considered finalized.

| ID | Open Issue | Required Action | Status |
|---|---|---|---|
| OI-01 | Technology stack not yet confirmed | Agree on the programming language, application framework, and database. | Pending confirmation |
| OI-02 | Final user roles and permissions | Confirm which user roles will be supported and define their permitted operations. | Pending confirmation |
| OI-03 | Database schema | Define the final tables, fields, primary keys, foreign keys, and constraints. | Pending design |
| OI-04 | API implementation details | Confirm endpoint paths, request and response formats, and error conventions. | Pending design |
| OI-05 | Authentication mechanism | Decide whether authentication is required and select the implementation approach. | Pending confirmation |
| OI-06 | Notification behaviour | Confirm how expiry and maintenance alerts will be generated and displayed. | Pending confirmation |
| OI-07 | Deployment environment | Determine how the application and database will be run and accessed. | Pending confirmation |
| OI-08 | Backup and recovery | Define suitable backup and recovery arrangements for stored data. | Pending design |

The statuses above are initial planning statuses. The team should update them as decisions are made and work is completed.

## 4.6.2 Next Steps

The following activities are proposed for the next stages of the project:

1. **Confirm Requirements:** Review the final SRS and ensure that the design supports the agreed functional, non-functional, and security requirements.
2. **Finalize Technologies:** Agree on the programming language, framework, database, and development tools.
3. **Finalize Database Design:** Define the database schema and relationships between assets, allocations, licenses, warranties, maintenance records, and users as applicable.
4. **Implement Core Components:** Develop the asset registration, search, update, allocation, and maintenance functions according to the agreed project scope.
5. **Implement Security Controls:** Develop and verify the required authentication, authorization, and input validation controls where applicable.
6. **Develop the User Interface:** Build the screens and workflows described in the UX design section.
7. **Execute Planned Tests:** Use the STP to test implemented functionality and record actual results and defects.
8. **Maintain Traceability:** Update the SAD and RTM when requirements or design decisions change.
9. **Review the Documentation:** Ensure that the final diagrams, interfaces, technology choices, and component descriptions match the implemented system.

## 4.6.3 Completion Criteria

The design documentation will be ready for final review when the open issues have been resolved or explicitly accepted, the architecture is consistent with the final requirements, the necessary diagrams and interfaces are documented, and the design reflects the team's agreed implementation approach.

Implementation and test completion must be assessed separately using actual project evidence.
