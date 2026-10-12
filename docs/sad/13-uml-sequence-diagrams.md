# 4.2 UML Sequence Diagrams

UML sequence diagrams illustrate the interactions between users and system components over time. The following diagrams represent two important workflows in the proposed IT Infrastructure & Asset Management System.

These diagrams describe the planned system behaviour and should be updated if the final implementation differs.

## 4.2.1 Sequence Diagram — Asset Registration

This diagram illustrates how an IT Administrator registers a new asset. The system validates the submitted information and checks for duplicate asset identifiers before saving the record.

```mermaid
sequenceDiagram
    actor Admin as IT Administrator
    participant UI as Web Interface
    participant App as Application Server
    participant Asset as Asset Management Module
    participant DB as Database

    Admin->>UI: Enter asset details
    UI->>App: Submit registration request
    App->>Asset: Validate asset information
    Asset->>DB: Check unique asset identifier
    DB-->>Asset: Return identifier check result

    alt Identifier is unique and data is valid
        Asset->>DB: Save new asset record
        DB-->>Asset: Confirm save
        Asset-->>App: Registration successful
        App-->>UI: Return success response
        UI-->>Admin: Display confirmation
    else Invalid data or duplicate identifier
        Asset-->>App: Return validation error
        App-->>UI: Return error response
        UI-->>Admin: Display error message
    end
```

**Explanation:** The administrator submits asset details through the interface. The application validates the information and checks the identifier before saving the record. If validation fails or the identifier already exists, the system should display an appropriate error instead of confirming successful registration.

## 4.2.2 Sequence Diagram — Asset Allocation

This diagram illustrates how an IT Administrator allocates an available asset to a user. The system checks asset availability before recording the allocation.

```mermaid
sequenceDiagram
    actor Admin as IT Administrator
    participant UI as Web Interface
    participant App as Application Server
    participant Alloc as Allocation Management Module
    participant DB as Database

    Admin->>UI: Select asset and assignee
    UI->>App: Submit allocation request
    App->>Alloc: Process allocation request
    Alloc->>DB: Retrieve asset status
    DB-->>Alloc: Return current status

    alt Asset is available
        Alloc->>DB: Record allocation and update status
        DB-->>Alloc: Confirm update
        Alloc-->>App: Allocation successful
        App-->>UI: Return success response
        UI-->>Admin: Display allocation confirmation
    else Asset is unavailable
        Alloc-->>App: Reject allocation request
        App-->>UI: Return availability error
        UI-->>Admin: Display error message
    end
```

**Explanation:** The administrator selects an asset and the intended assignee. The system checks whether the asset is available. If available, it records the allocation and updates the asset status. Otherwise, it rejects the request and displays an appropriate message.

## 4.2.3 Design Considerations

- Asset identifiers should be unique to prevent duplicate asset records.
- Asset availability should be checked before an allocation is confirmed.
- Database updates should maintain consistency between allocation records and asset status.
- Failed operations should return clear error messages.
- The final implementation should handle concurrent requests so that the same asset is not allocated to multiple users simultaneously.

These diagrams describe the intended workflows. Actual behaviour must be verified through implementation and testing.
