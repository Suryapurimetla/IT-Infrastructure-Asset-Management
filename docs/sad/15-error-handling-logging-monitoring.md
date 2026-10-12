# 4.4 Error Handling, Logging & Monitoring

## 4.4.1 Overview

The IT Infrastructure & Asset Management System should handle errors in a consistent manner to support reliability, data integrity, security, and ease of maintenance.

The proposed error-handling approach covers invalid input, unavailable records, database failures, unauthorized operations, and unexpected application errors. Logging and monitoring mechanisms should help the development and maintenance team identify issues when these mechanisms are implemented.

## 4.4.2 Error Handling

The application should validate requests and handle expected errors before returning a response to the user.

The following error-handling rules are proposed:

| Error Scenario | Expected System Behaviour |
|---|---|
| Missing required fields | Reject the request and display a validation message. |
| Invalid field values | Identify the invalid input and explain what needs correction. |
| Duplicate asset identifier | Reject the registration and inform the user that the identifier already exists. |
| Asset not found | Display an appropriate message indicating that the requested asset could not be found. |
| Asset unavailable for allocation | Reject the allocation and explain that the asset is not available. |
| Unauthorized operation | Reject the request without performing the protected operation. |
| Database failure | Avoid confirming success, handle the failure safely, and inform the user that the operation could not be completed. |
| Unexpected application error | Return a general error message without exposing internal technical details. |

## 4.4.3 Logging

Application logging can help developers investigate failures and understand important system events.

The proposed logging approach includes:

- Recording significant application errors and exceptions.
- Recording relevant asset-management operations where appropriate.
- Recording failed operations that may require investigation.
- Including timestamps and useful context in log entries.
- Restricting access to logs to authorized personnel.
- Avoiding the storage of passwords, authentication secrets, or unnecessary sensitive information in logs.

The exact logging framework and log-storage location will depend on the final technology stack.

## 4.4.4 Monitoring

Monitoring should help identify application failures and operational problems during development and deployment.

Potential monitoring activities include:

- Checking application availability.
- Identifying repeated application or database errors.
- Observing response times for important operations.
- Checking database connectivity.
- Reviewing relevant error logs.
- Investigating repeated failed or unauthorized requests where security logging is implemented.

The monitoring tools and alerting mechanisms will be selected according to the project's deployment environment and available resources.

## 4.4.5 Data Integrity During Failures

The system should avoid leaving asset records in an inconsistent state when an operation fails.

For example, when an asset is allocated, the allocation record and asset status should be updated consistently. If either update fails, the application should use an appropriate transaction or recovery mechanism to avoid recording a partial allocation.

Similarly, a failed asset registration should not be reported as successful unless the record has actually been saved.

## 4.4.6 Security Considerations

Error messages shown to users should provide enough information to help them correct common problems without exposing internal database details, credentials, or implementation information.

Detailed diagnostic information should be available only through appropriately protected logs.

These error-handling, logging, and monitoring mechanisms are planned design requirements. Their actual implementation and effectiveness must be verified during testing.
