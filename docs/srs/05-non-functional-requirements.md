# 5. Non-functional requirements (detailed)

The following non-functional requirements define the quality, performance, reliability, and security expectations of the IT Infrastructure & Asset Management System. IDs follow the ITAM-NF-### format.

| Req ID | Requirement | Category | Priority | Acceptance criteria / Measurement |
|---|---|---|---|---|
| ITAM-NF-001 | The system shall display asset search results within 3 seconds for 90% of requests under normal test conditions. | Performance | High | 90% of measured searches complete within 3 seconds. Test: TC-NF-01 |
| ITAM-NF-002 | The system shall maintain accurate and consistent asset records during create, view, and update operations. | Reliability | High | Saved records can be retrieved with their stored values unchanged. Test: TC-NF-02 |
| ITAM-NF-003 | The system shall restrict protected operations to authorized users where authentication and access control are implemented. | Security | High | Unauthorized access to protected operations is denied. Test: TC-NF-03 |
| ITAM-NF-004 | The system shall provide clear navigation, readable information, and understandable validation messages. | Usability | Medium | Representative users can complete basic asset tasks without unclear or misleading messages. Test: TC-NF-04 |
| ITAM-NF-005 | The system shall validate user input and handle application or database errors without losing previously saved records. | Robustness | High | Invalid input is rejected, and simulated errors do not cause incorrect success messages or unintended record changes. Test: TC-NF-05 |

## 5.1. Security

### 5.1.1 Security Objectives

1. **Confidentiality:** Protect asset and allocation information from unauthorized access.
2. **Integrity:** Ensure asset records, allocation details, license information, and maintenance records are modified only through authorized operations.

### 5.1.2 Security Requirements

| Req ID | Requirement (shall...) | Type | Priority | Acceptance criteria / Test case ref |
|---|---|---|---|---|
| ITAM-SR-001 | The system shall require authentication before allowing access to protected functions, where authentication is implemented. | Security | High | Unauthenticated access to protected functions is denied. Test: TC-SEC-01 |
| ITAM-SR-002 | The system shall enforce role-based permissions for restricted operations where role-based access control is implemented. | Security | High | Users cannot perform operations outside their assigned permissions. Test: TC-SEC-02 |
| ITAM-SR-003 | The system shall validate and sanitize user input to reduce the risk of injection and malformed-data attacks. | Security | High | Invalid or malicious test inputs are rejected or handled safely. Test: TC-SEC-03 |
| ITAM-SR-004 | The system shall protect sensitive information during network transmission using secure communication mechanisms appropriate to the deployment. | Security | High | Network communication uses the configured secure transport where applicable. Test: TC-SEC-04 |
| ITAM-SR-005 | The system shall avoid storing passwords or other authentication secrets in plaintext if authentication credentials are stored by the application. | Security | High | Inspection confirms credentials are not stored in plaintext. Test: TC-SEC-05 |
