# 3. External interface requirements

## 3.1 User interfaces

The system shall provide a user interface through which authorized users can register, view, search, and update IT asset records.

The interface shall provide clear navigation for asset management, allocation, license and warranty tracking, and maintenance records. Forms shall display appropriate validation messages when required information is missing or invalid.

The interface should present asset status and relevant expiry or maintenance information clearly. The layout shall be easy to understand and use for the intended users.

## 3.2 Hardware interfaces

- The system shall operate on a computer or laptop capable of running the selected application environment.
- The system may be accessed through standard input devices such as a keyboard and mouse or a compatible touchscreen.
- No direct interface with physical IT asset hardware is required for the core project scope.
- Hardware asset information, such as model number and serial number, shall be recorded through the application where applicable.

## 3.3 Software interfaces

- **Database interface:** The application shall communicate with its configured database to store, retrieve, and update asset information.
- **Application interface:** The user interface shall communicate with the application logic to perform authorized operations.
- **Operating system:** The application shall use the services and runtime provided by its supported operating environment.
- **External services:** Integration with email, notification, inventory, or other external services is not mandatory unless included in the final implementation.

## 3.4 Communications

- Communication between the user interface and application components shall use the mechanisms supported by the selected implementation.
- If the system is deployed over a network, communication shall use appropriate security measures.
- The system shall handle communication or database errors without displaying misleading success messages.
- Any external API communication implemented in the project shall use the authentication and protection mechanisms appropriate to that interface.
