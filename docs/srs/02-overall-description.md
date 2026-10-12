# 2. Overall description

## 2.1 Product perspective

The IT Infrastructure & Asset Management System is a centralized application used to maintain and manage an organization's IT assets. It provides a common platform for storing asset details, tracking allocation, managing software licenses and warranties, and recording maintenance activities.

The system organizes asset information so that authorized users can access and update records efficiently. It is designed as a standalone project application, with its actual interfaces and dependencies determined by the final implementation.

## 2.2 Major product functions (detailed)

- Register hardware and software assets.
- Assign unique identifiers to asset records.
- View, search, filter, and update asset information.
- Maintain asset details such as category, model, serial number, and status.
- Track asset allocation to users or departments.
- Record software license information and expiry dates.
- Maintain warranty information and expiry dates.
- Record asset maintenance activities.
- Identify assets requiring maintenance or renewal.
- Generate notifications or alerts for upcoming expiry dates where implemented.
- Validate input data and handle invalid entries.
- Restrict access to authorized functions where access control is implemented.
- Maintain accurate and consistent asset records.

## 2.3 User roles and characteristics (expanded)

- **IT Administrator:** Maintains asset records, manages allocations, updates license and warranty details, and monitors maintenance activities.
- **Staff / Asset User:** Views assigned asset information and reports asset-related issues where the relevant functionality is available.
- **Maintenance Personnel:** Reviews maintenance records and updates maintenance status where authorized.
- **Project Evaluator:** Reviews the system's functionality and verifies whether the documented requirements are satisfied.

## 2.4 Operating environment

The system will operate in the software environment selected for the project implementation. Users will access the application through the supported interface and operating environment. The application will require its configured database, runtime, and other necessary dependencies.

The exact operating system, browser support, database, and runtime will be documented according to the final implementation.

## 2.5 Constraints

- The system must follow the approved project scope and requirements.
- Asset records must be validated to maintain data accuracy and consistency.
- Access to restricted operations must be controlled where authentication and authorization are implemented.
- The system depends on the availability of its configured application environment and database.
- Notifications, reporting, and other additional features will depend on their implementation in the project.
- The system will use sample or authorized asset data during development and testing.
