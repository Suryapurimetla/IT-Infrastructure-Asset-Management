# 3.4 Component Descriptions

The following table describes the major components shown in the UML component diagram of the IT Infrastructure & Asset Management System. Each component has a defined responsibility to support modularity, maintainability, and clear separation of concerns.

| Component | Type | Description | Key Responsibilities |
|---|---|---|---|
| Web Browser (Web Client) | External Client | Client application used to access the system through a web browser. | Sends user requests and displays responses from the system. |
| IT Administrator | External Actor | User responsible for managing IT asset information. | Registers assets, updates records, searches assets, and manages allocation and maintenance information according to permissions. |
| Authorized User | External Actor | User permitted to access specific system functions. | Views asset information and performs permitted operations. |
| Web Interface (UI) | User Interface | Interface through which users interact with the application. | Accepts user input, displays asset details, and presents operation results and validation messages. |
| Application Server (Business Logic) | Core Component | Processes requests and coordinates the functional modules. | Applies business rules, validates requests, enforces access permissions where implemented, and coordinates data operations. |
| Asset Management Module | Functional Module | Manages hardware and software asset records. | Registers assets, searches records, displays details, and updates asset information. |
| Allocation Management Module | Functional Module | Manages asset allocation and availability. | Records allocations, updates asset status, and supports returns and reassignments. |
| License & Warranty Management Module | Functional Module | Maintains software license and hardware warranty details. | Records and updates license and warranty information and supports expiry tracking. |
| Maintenance Management Module | Functional Module | Manages asset maintenance information. | Records maintenance activities, updates maintenance status, and tracks upcoming maintenance events. |
| Notification Module | Functional Module | Supports identification of upcoming expiry and maintenance events. | Identifies relevant dates and supports alerts for upcoming or overdue events, subject to implementation. |
| Database (Asset Data) | Data Store | Stores persistent information used by the system. | Stores and retrieves asset, allocation, license, warranty, maintenance, and relevant user records. |

### Component Interaction

The components interact according to the following planned workflow:

1. The IT Administrator or Authorized User accesses the system using a web browser.
2. The Web Interface receives user input and sends requests to the Application Server.
3. The Application Server validates requests and coordinates the appropriate functional module.
4. The selected module performs the required operation using the relevant data.
5. The Database stores or retrieves the necessary information.
6. The system returns the result to the Web Interface, which displays it to the user.

The exact component boundaries and communication mechanisms may be refined during implementation. This description represents the proposed design and should be updated if the final implementation differs.
