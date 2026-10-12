# 3. Architecture

## 3.1 Goals & Constraints

### 3.1.1 Architecture Goals

The architecture of the IT Infrastructure & Asset Management System is planned to meet the following goals:

1. **Modularity:** Separate the system into components with clearly defined responsibilities, such as asset management, allocation, maintenance, and reporting.
2. **Maintainability:** Organize the design so that components can be updated or improved without requiring unnecessary changes to unrelated components.
3. **Data Consistency:** Maintain accurate and consistent asset information when assets are registered, updated, allocated, returned, or assigned for maintenance.
4. **Security:** Support authentication, role-based access control, input validation, and protection of sensitive information, according to the security requirements defined in the SRS.
5. **Usability:** Provide a straightforward interface through which authorized users can manage and search IT asset records.
6. **Testability:** Design components and interfaces so that their expected behaviour can be verified using the test cases defined in the STP.
7. **Extensibility:** Allow future enhancements, such as additional asset categories, reports, and notification mechanisms, without redesigning the entire system.

### 3.1.2 Architecture Constraints

The architecture and implementation are subject to the following constraints:

1. **Project Scope:** The design must support the functional and non-functional requirements documented in the Software Requirements Specification (SRS).
2. **Project Schedule:** The architecture must remain practical for the available academic project timeline and the team's development resources.
3. **Team Resources:** The selected design and technologies must be manageable by the project team.
4. **Requirement Traceability:** Architecture components and design decisions should be traceable to relevant requirements wherever applicable.
5. **Technology Selection:** The final programming language, framework, database, and deployment environment must be confirmed by the team before they are documented as the actual implementation stack.
6. **Testing Requirements:** The design must allow the planned test cases and security checks in the Software Test Plan (STP) to be carried out.
7. **Implementation Status:** Components described in this document represent the planned design unless implementation has been completed and verified.

These goals and constraints will guide the selection of the architecture pattern, component responsibilities, interfaces, data storage approach, and security mechanisms in the following sections.
