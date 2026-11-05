# 8. Requirements Traceability Matrix (RTM)

The RTM maps system requirements to their corresponding design sections, application modules and test cases. It helps track requirement validation and testing progress.

## 8.1 Functional Requirements

| Req ID | Requirement / Short Description | Section Ref | Module | Test Case(s) | Status | Comments |
|---|---|---|---|---|---|---|
| ITAM-F-001 | Register hardware and software assets | 4.1 | Asset Management | TC-ITAM-01 | P | Asset registration manually tested |
| ITAM-F-002 | Maintain unique asset identifiers | 4.1 | Asset Management | TC-ITAM-02 | P | Duplicate ID rejection manually tested |
| ITAM-F-003 | Validate mandatory asset fields | 4.1 | Asset Management | TC-ITAM-03 | P | Required-field validation manually tested |
| ITAM-F-004 | View and search asset records | 4.1 | Asset Management | TC-ITAM-04 | P | Automated asset-name search test passed |
| ITAM-F-005 | Update asset information | 4.1 | Asset Management | TC-ITAM-05 | P | Asset editing manually tested |
| ITAM-F-006 | Allocate assets to staff or departments | 4.2 | Allocation Management | TC-ITAM-06 | N | Requires further validation |
| ITAM-F-007 | Maintain current asset status | 4.2 | Allocation Management | TC-ITAM-07 | N | Requires further validation |
| ITAM-F-008 | Record asset return or reassignment | 4.2 | Allocation Management | TC-ITAM-08 | N | Requires further validation |
| ITAM-F-009 | Record software license details | 4.3 | License Management | TC-ITAM-09 | N | Requires further validation |
| ITAM-F-010 | Maintain hardware warranty details | 4.3 | Warranty Management | TC-ITAM-10 | N | Requires further validation |
| ITAM-F-011 | Identify expired or upcoming license and warranty dates | 4.3 | Expiry Tracking | TC-ITAM-11 | N | Requires further validation |
| ITAM-F-012 | Record maintenance activities | 4.4 | Maintenance Management | TC-ITAM-12 | N | Requires further validation |
| ITAM-F-013 | Update maintenance status | 4.4 | Maintenance Management | TC-ITAM-13 | N | Requires further validation |
| ITAM-F-014 | Identify upcoming or overdue maintenance | 4.4 | Maintenance Management | TC-ITAM-14 | N | Requires further validation |
| ITAM-F-015 | Display relevant expiry or maintenance alerts | 4.4 | Notification Management | TC-ITAM-15 | N | Requires further validation |
| ITAM-F-016 | Delete existing asset records | 4.1 | Asset Management | TC-ITAM-16 | P | Test asset deletion manually tested |

## 8.2 Non-Functional Requirements

| Req ID | Requirement / Short Description | Section Ref | Module | Test Case(s) | Status | Comments |
|---|---|---|---|---|---|---|
| ITAM-NF-001 | Meet asset search response-time target | 5 | Application | TC-NF-01 | N | Not tested |
| ITAM-NF-002 | Maintain accurate and consistent records | 5 | Database / Application | TC-NF-02 | N | Not tested |
| ITAM-NF-003 | Restrict unauthorized access | 5 | Access Control | TC-NF-03 | N | Not tested |
| ITAM-NF-004 | Provide clear and usable interfaces | 5 | User Interface | TC-NF-04 | N | Not tested |
| ITAM-NF-005 | Handle invalid input and application errors safely | 5 | Application | TC-NF-05 | N | Not tested |

## 8.3 Security Requirements

| Req ID | Requirement / Short Description | Section Ref | Module | Test Case(s) | Status | Comments |
|---|---|---|---|---|---|---|
| ITAM-SR-001 | Require authentication for protected functions | 5.1.2 | Authentication | TC-SEC-01 | N | Not tested |
| ITAM-SR-002 | Enforce role-based permissions | 5.1.2 | Access Control | TC-SEC-02 | N | Not tested |
| ITAM-SR-003 | Validate and sanitize user input | 5.1.2 | Input Validation | TC-SEC-03 | N | Not fully tested |
| ITAM-SR-004 | Protect sensitive information during network transmission | 5.1.2 | Communication Security | TC-SEC-04 | N | Not tested |
| ITAM-SR-005 | Avoid storing authentication secrets in plaintext | 5.1.2 | Credential Security | TC-SEC-05 | N | Not tested |

## 8.4 Status Legend

- **N** – Not Run
- **P** – Pass
- **A** – Fail

The status of each requirement is based on the available test execution evidence. Requirements marked Not Run require further validation.

The RTM should be reviewed whenever requirements, application features or test cases change.