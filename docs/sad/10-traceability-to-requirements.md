# 3.8 Traceability to Requirements

## 3.8.1 Purpose

Traceability establishes the relationship between the requirements defined in the Software Requirements Specification (SRS) and the architectural components designed for the IT Infrastructure & Asset Management System.

This mapping helps ensure that the proposed architecture supports the required system functionality and provides a basis for planning implementation and testing activities.

## 3.8.2 Requirements-to-Architecture Mapping

| Requirement ID | Requirement Description | Related Architectural Component |
|---|---|---|
| ITAM-F-001 | Asset registration | Asset Management Module |
| ITAM-F-002 | Unique asset identification | Asset Management Module, Database |
| ITAM-F-003 | Input validation | Application Server, Asset Management Module |
| ITAM-F-004 | Asset search | Asset Management Module, Database |
| ITAM-F-005 | View asset details | Web Interface, Asset Management Module |
| ITAM-F-006 | Update asset information | Asset Management Module, Database |
| ITAM-F-007 | Asset allocation | Allocation Management Module |
| ITAM-F-008 | Asset status management | Allocation Management Module, Database |
| ITAM-F-009 | Asset return and reassignment | Allocation Management Module |
| ITAM-F-010 | Software license management | License & Warranty Management Module |
| ITAM-F-011 | Warranty information management | License & Warranty Management Module |
| ITAM-F-012 | Expiry alerts | Notification Module |
| ITAM-F-013 | Maintenance record management | Maintenance Management Module |
| ITAM-F-014 | Maintenance status tracking | Maintenance Management Module |
| ITAM-F-015 | Upcoming maintenance identification | Maintenance Management Module, Notification Module |

**Note:** The descriptions above summarize the planned requirements. Verify each description against the final SRS before submission.

## 3.8.3 Non-Functional and Security Requirements

| Requirement ID | Requirement Area | Related Architectural Component |
|---|---|---|
| ITAM-NF-001 | Performance | Application Server, Database |
| ITAM-NF-002 | Data consistency | Application Server, Database |
| ITAM-NF-003 | Access control | Application Server, Web Interface |
| ITAM-NF-004 | Usability | Web Interface |
| ITAM-NF-005 | Robustness and error handling | Application Server, Database |
| ITAM-SR-001 | Authentication | Web Interface, Application Server |
| ITAM-SR-002 | Role-based access control | Application Server |
| ITAM-SR-003 | Input sanitization and validation | Web Interface, Application Server |
| ITAM-SR-004 | Secure communication | Web Interface, Application Server |
| ITAM-SR-005 | Protection of authentication information | Application Server, Database |

## 3.8.4 Traceability and Verification

The mapping identifies which components are expected to support each requirement. During implementation, the team should verify that the relevant components provide the required behaviour.

The Software Test Plan (STP) and Requirements Traceability Matrix (RTM) should be used to connect requirements to planned test cases and record verification results. Requirements should not be marked as implemented or passed until appropriate evidence is available.

Any changes to requirement IDs or descriptions in the final SRS must be reflected in this section and the corresponding STP documentation.

