# 3.5 Chosen Architecture Pattern and Rationale

## 3.5.1 Selected Architecture Pattern

The proposed architecture for the IT Infrastructure & Asset Management System follows a **Layered Architecture Pattern**. The system is divided into logical layers, with each layer responsible for a specific set of functions.

The proposed layers are:

1. **Presentation Layer:** Provides the web interface through which administrators and authorized users interact with the system.
2. **Application and Business Logic Layer:** Processes user requests, validates input, applies business rules, and coordinates asset-related operations.
3. **Data Access Layer:** Handles communication between the application logic and the database.
4. **Data Storage Layer:** Stores persistent information about assets, allocations, software licenses, warranties, maintenance records, and relevant user information.

## 3.5.2 Rationale for Selection

The Layered Architecture Pattern is suitable for this project for the following reasons:

- **Separation of Concerns:** The user interface, business rules, and data storage have distinct responsibilities.
- **Maintainability:** Changes to one layer can often be made without major changes to unrelated layers, provided the interfaces remain stable.
- **Testability:** Individual layers and their interactions can be tested against the requirements specified in the SRS and the test cases planned in the STP.
- **Simplicity:** The pattern is straightforward to understand and implement within an academic project timeline.
- **Extensibility:** Additional functions, such as new asset categories or reporting features, can be introduced as the system evolves.
- **Data Management:** A dedicated data access layer helps organize database operations and supports consistent handling of asset information.

## 3.5.3 Architectural Flow

The expected request flow is:

1. A user performs an operation through the Presentation Layer.
2. The Application and Business Logic Layer receives the request and validates the required information.
3. The Data Access Layer retrieves or updates information in the database when necessary.
4. The result is returned through the application layer to the Presentation Layer.
5. The user interface displays the result or an appropriate validation or error message.

## 3.5.4 Limitations and Considerations

The layered approach introduces some additional structure and requires clear interfaces between layers. Poorly defined responsibilities may lead to duplicated logic or unnecessary dependencies. These risks will be reduced by keeping component responsibilities clear and maintaining consistent interfaces.

The architecture pattern described here is the proposed design. The team should verify that it matches the actual implementation before submitting the final SAD document.
