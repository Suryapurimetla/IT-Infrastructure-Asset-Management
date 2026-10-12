# 4. Design

## 4.1 Design Overview

The design of the IT Infrastructure & Asset Management System describes how the proposed architecture will support the system requirements. The design focuses on organizing system functions into components, defining interactions between them, managing asset information, and supporting security and maintainability.

The system is intended to provide a centralized way to manage IT assets, including asset registration, searching, updating, allocation, license and warranty tracking, and maintenance management.

### 4.1.1 Design Principles

The following principles guide the proposed system design:

1. **Modularity:** Divide the system into components with clear responsibilities, such as asset management, allocation management, license and warranty management, maintenance management, and notifications.
2. **Separation of Concerns:** Keep user interface responsibilities separate from business logic and data storage operations.
3. **Data Integrity:** Use validation and suitable database constraints to help maintain accurate asset information.
4. **Security:** Apply appropriate authentication, authorization, and input validation controls according to the final requirements and implementation.
5. **Maintainability:** Organize the design so that individual components can be modified with minimal impact on unrelated functionality.
6. **Testability:** Define clear component responsibilities and interactions so that the system can be tested against the SRS and STP.
7. **Usability:** Provide a straightforward interface for common asset management tasks.

### 4.1.2 Main Design Components

The proposed design consists of the following components:

- **Web Browser (Web Client):** Provides the environment through which users access the system.
- **Web Interface (UI):** Accepts user input and displays asset information, operation results, and error messages.
- **Application Server:** Processes requests, applies business rules, and coordinates operations.
- **Asset Management Module:** Handles asset registration, search, viewing, and updates.
- **Allocation Management Module:** Handles asset allocation, returns, reassignment, and availability status.
- **License and Warranty Management Module:** Manages license and warranty information.
- **Maintenance Management Module:** Maintains maintenance records and maintenance status.
- **Notification Module:** Supports identification of upcoming expiry and maintenance events.
- **Database:** Stores the persistent information required by the system.

### 4.1.3 General Processing Flow

The planned processing flow for a typical operation is as follows:

1. The user opens the system through a web browser.
2. The user selects an operation, such as registering a new asset or searching for an existing asset.
3. The Web Interface collects the required input and sends the request to the Application Server.
4. The Application Server validates the request and checks the applicable business rules and permissions.
5. The relevant functional module performs the requested operation.
6. The Database is accessed when information needs to be retrieved or updated.
7. The application returns the result to the Web Interface.
8. The interface displays the result or an appropriate validation or error message.

### 4.1.4 Data Design Considerations

The system will manage related categories of information, including assets, allocations, licenses, warranties, maintenance activities, and relevant user records.

Each asset should have a unique identifier. Related records should reference the relevant asset where appropriate, helping prevent inconsistent or disconnected information.

The detailed database schema, relationships, and constraints will be finalized during implementation according to the selected database technology.

### 4.1.5 Relationship to UML Diagrams

The component diagram in Section 3.3 presents the proposed structural organization of the system. The sequence diagrams in Section 4.2 will illustrate how components interact during selected operations, including asset registration and asset allocation.

Together, these diagrams will describe the planned structure and behaviour of the system. They should be updated if the final implementation differs from the proposed design.

