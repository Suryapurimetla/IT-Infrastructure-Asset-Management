# 3.6 Technology Stack & Data Stores

## 3.6.1 Proposed Technology Stack

The technology stack for the IT Infrastructure & Asset Management System will be selected based on the project requirements, the team's technical knowledge, and the available development time.

The following table presents a possible technology stack. These choices must be confirmed by the team before they are treated as final.

| Layer | Proposed Technology | Purpose |
|---|---|---|
| Presentation Layer | HTML, CSS, JavaScript | Provides the user interface for asset management operations. |
| Application Layer | Python with Flask | Processes application requests and implements business logic. |
| Data Access Layer | Flask database integration or a suitable Python database library | Connects application logic with the database. |
| Data Storage Layer | MySQL | Stores asset information and related records. |
| Diagramming | Draw.io | Creates UML diagrams for the SAD document. |
| Version Control | Git and GitHub | Maintains source code, documentation, branches, and pull requests. |
| Testing | Python testing framework, if Python is selected | Supports automated verification of application behaviour. |

## 3.6.2 Data Stores

The system is expected to use a relational database to organize and maintain structured information. MySQL is listed as a proposed option; the final database technology must be confirmed by the team.

The planned categories of stored information include:

- **Asset Records:** Asset identifier, name, category, description, serial number, and status.
- **Allocation Records:** Asset allocation details, assigned user or department, allocation date, and return information.
- **License Records:** Software license details, validity dates, and relevant renewal information.
- **Warranty Records:** Warranty start date, expiry date, and related information.
- **Maintenance Records:** Asset reference, maintenance description, maintenance date, and status.
- **User Records:** Relevant account details and role or permission information, according to the final security design.

The exact database tables, fields, keys, relationships, and constraints will be defined during implementation.

## 3.6.3 Data Management Considerations

The database design should support accurate and consistent asset records. Each asset should have a unique identifier, and related records should reference the appropriate asset. Validation rules should prevent incomplete or invalid data from being stored where applicable.

Access to stored information should be controlled according to the security requirements documented in the SRS. Sensitive authentication information must not be stored in plaintext if authentication is included in the implementation.

Database backups, recovery procedures, and deployment configuration should be considered as the implementation progresses.

## 3.6.4 Technology Confirmation

Before implementation, the project team should agree on the programming language, framework, database, and testing tools. The final version of this section must reflect the technologies actually selected for the project.

