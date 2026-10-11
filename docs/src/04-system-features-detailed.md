# 4. System features (detailed)

Each requirement includes a unique requirement ID, requirement description, type, priority, source/stakeholder, acceptance criteria, and comments/dependencies. IDs follow the ITAM-F-### format.

## 4.1 Asset Registration and Management

Description: This feature allows authorized users to register and maintain hardware and software asset records.

| Req ID | Requirement | Type | Priority | Source/Stakeholder | Acceptance criteria / Test case ref | Comments / Dependencies |
|---|---|---|---|---|---|---|
| ITAM-F-001 | The system shall allow authorized users to register hardware and software assets with the required details. | Functional | High | IT Administrator | A valid asset record is saved and can be retrieved. Test: TC-ITAM-01 | Requires database storage. |
| ITAM-F-002 | The system shall assign or record a unique identifier for each asset. | Functional | High | IT Administrator | Each registered asset has a unique identifier. Test: TC-ITAM-02 | Duplicate identifiers must be rejected. |
| ITAM-F-003 | The system shall validate mandatory asset fields before saving a record. | Functional | High | IT Administrator | Records with missing mandatory fields are rejected with an appropriate message. Test: TC-ITAM-03 | Depends on input validation. |
| ITAM-F-004 | The system shall allow authorized users to view and search asset records. | Functional | High | IT Administrator / Staff | A search returns matching records for the entered criteria. Test: TC-ITAM-04 | Search fields depend on implementation. |
| ITAM-F-005 | The system shall allow authorized users to update existing asset information. | Functional | High | IT Administrator | Updated details are saved and displayed correctly. Test: TC-ITAM-05 | Requires an existing asset record. |

## 4.2 Asset Allocation and Status

Description: This feature manages asset assignments and current asset status.

| Req ID | Requirement | Type | Priority | Source/Stakeholder | Acceptance criteria / Test case ref | Comments / Dependencies |
|---|---|---|---|---|---|---|
| ITAM-F-006 | The system shall allow authorized users to allocate an available asset to a staff member or department. | Functional | High | IT Administrator | The allocation is recorded against the selected asset and user or department. Test: TC-ITAM-06 | Requires allocation details. |
| ITAM-F-007 | The system shall maintain the current status of each asset. | Functional | High | IT Administrator | The asset status is displayed accurately after a status update. Test: TC-ITAM-07 | Status values must be defined. |
| ITAM-F-008 | The system shall allow authorized users to record the return or reassignment of an allocated asset. | Functional | Medium | IT Administrator | The allocation record is updated after return or reassignment. Test: TC-ITAM-08 | Requires allocation history. |

## 4.3 License and Warranty Tracking

Description: This feature maintains software license and asset warranty information.

| Req ID | Requirement | Type | Priority | Source/Stakeholder | Acceptance criteria / Test case ref | Comments / Dependencies |
|---|---|---|---|---|---|---|
| ITAM-F-009 | The system shall allow authorized users to record software license details and expiry dates. | Functional | High | IT Administrator | License details and expiry dates are saved and retrievable. Test: TC-ITAM-09 | Applies to software licenses. |
| ITAM-F-010 | The system shall maintain warranty details for applicable hardware assets. | Functional | High | IT Administrator | Warranty information is linked to the relevant asset record. Test: TC-ITAM-10 | Requires warranty data. |
| ITAM-F-011 | The system shall identify licenses and warranties that are approaching or have passed their expiry dates. | Functional | Medium | IT Administrator | Expired and upcoming expiry records are identified correctly. Test: TC-ITAM-11 | Depends on stored expiry dates. |

## 4.4 Maintenance and Notifications

Description: This feature records maintenance activities and identifies assets requiring attention.

| Req ID | Requirement | Type | Priority | Source/Stakeholder | Acceptance criteria / Test case ref | Comments / Dependencies |
|---|---|---|---|---|---|---|
| ITAM-F-012 | The system shall allow authorized users to record maintenance activities for an asset. | Functional | High | Maintenance Personnel | The maintenance record is saved against the correct asset. Test: TC-ITAM-12 | Requires an existing asset. |
| ITAM-F-013 | The system shall allow authorized users to update the status of a maintenance activity. | Functional | Medium | Maintenance Personnel | The updated maintenance status is displayed correctly. Test: TC-ITAM-13 | Status values must be defined. |
| ITAM-F-014 | The system shall identify assets with upcoming maintenance dates or overdue maintenance where such dates are recorded. | Functional | Medium | IT Administrator | Assets due for maintenance are identified based on their recorded dates. Test: TC-ITAM-14 | Depends on maintenance scheduling data. |
| ITAM-F-015 | The system shall display or generate alerts for relevant license, warranty, or maintenance events where notification functionality is implemented. | Functional | Medium | IT Administrator | A qualifying event produces the configured alert. Test: TC-ITAM-15 | Delivery channels depend on implementation.
