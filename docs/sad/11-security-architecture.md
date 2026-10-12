# 3.9 Security Architecture

## 3.9.1 Overview

The security architecture of the IT Infrastructure & Asset Management System is intended to protect asset information from unauthorized access, improper modification, and accidental disclosure.

The proposed security design follows the security objectives and requirements defined in the Software Requirements Specification (SRS). Security mechanisms should be incorporated into the user interface, application logic, and data storage layers as appropriate.

## 3.9.2 Authentication

Authentication verifies the identity of users before allowing access to protected system functions, if user authentication is included in the final implementation.

The proposed authentication mechanism should:
- Require users to provide valid credentials.
- Reject invalid authentication attempts.
- Avoid storing passwords in plaintext.
- Protect authentication information during transmission.
- Prevent unauthenticated users from accessing protected operations.

The specific authentication method will be selected during implementation.

## 3.9.3 Authorization and Role-Based Access Control

Authorization determines which operations an authenticated user is permitted to perform.

The proposed design uses role-based access control (RBAC), subject to confirmation of the final user roles and permissions.

For example:
- **IT Administrator:** May be permitted to register, update, search, and manage asset records.
- **Authorized User:** May be permitted to view selected asset information and perform approved operations.

The application logic should verify permissions before executing protected operations. Hiding a function in the user interface alone is not sufficient to enforce access control.

## 3.9.4 Input Validation and Data Protection

Input validation helps prevent invalid or unexpected data from entering the system.

The proposed measures include:
- Checking required fields and data formats.
- Validating asset identifiers and relevant dates.
- Rejecting invalid values before database operations.
- Using parameterized database queries or equivalent safe data-access methods.
- Applying appropriate database constraints to preserve data consistency.

These measures should be implemented and tested according to the relevant functional and security requirements in the SRS.

## 3.9.5 Secure Communication

If the application is deployed over a network, HTTPS should be used to protect communication between the user's browser and the application server.

The deployment configuration should use valid TLS certificates and avoid transmitting credentials or other sensitive information through unencrypted connections.

The final communication configuration will depend on the deployment environment selected by the team.

## 3.9.6 Database Security

The database should be protected against unauthorized access and improper modification.

The proposed measures include:
- Restricting database access to authorized application components and administrators.
- Using appropriate database accounts and permissions.
- Avoiding hard-coded or publicly exposed database credentials.
- Protecting configuration files containing sensitive information.
- Planning suitable backup and recovery procedures.
- Applying database constraints to maintain data integrity.

## 3.9.7 Error Handling and Logging

Errors should be handled without unnecessarily exposing sensitive information.

The application should:
- Display understandable error messages to users.
- Avoid exposing passwords, credentials, or internal database details in user-facing messages.
- Record relevant operational and security events where logging is implemented.
- Restrict access to logs that may contain sensitive information.
- Avoid recording passwords or other unnecessary secrets in logs.

## 3.9.8 Security Requirement Mapping

| Security Requirement ID | Security Control | Architectural Location |
|---|---|---|
| ITAM-SR-001 | Authentication | Web Interface and Application Server |
| ITAM-SR-002 | Role-based access control | Application Server |
| ITAM-SR-003 | Input sanitization and validation | Web Interface and Application Server |
| ITAM-SR-004 | Secure communication | Browser-to-Application Server connection |
| ITAM-SR-005 | Protection of authentication information | Application Server and Database |

## 3.9.9 Security Verification

The planned security controls should be verified through appropriate test cases defined in the Software Test Plan (STP). Verification should include unauthorized access attempts, permission checks, invalid input handling, and protection of authentication information where those features are implemented.

The security controls described in this section are design intentions, not evidence of completed implementation or successful testing. The final SAD should be updated to reflect the security mechanisms actually selected and implemented.

