# 4.3 API Design

## 4.3.1 Overview

The proposed API design defines how the Web Interface communicates with the application logic to perform asset management operations. The interfaces below describe two core components: Asset Management and Allocation Management.

The API contracts use HTTP methods and JSON request and response examples. The final endpoint paths, authentication mechanisms, and data formats should be confirmed during implementation.

## 4.3.2 Component 1 — Asset Management API

**Purpose:** Provides operations for registering, retrieving, searching, and updating IT asset records.

### Proposed Interface Definition

| Operation | HTTP Method | Endpoint | Purpose |
|---|---|---|---|
| Register asset | POST | `/api/assets` | Creates a new asset record. |
| List assets | GET | `/api/assets` | Retrieves asset records, subject to access permissions. |
| Get asset details | GET | `/api/assets/{assetId}` | Retrieves a specific asset by its identifier. |
| Update asset | PUT | `/api/assets/{assetId}` | Updates an existing asset record. |

### Example Request — Register Asset

```http
POST /api/assets
Content-Type: application/json
```

```json
{
  "name": "Laptop",
  "category": "Hardware",
  "serialNumber": "SN10025",
  "status": "Available"
}
```

### Example Success Response

```json
{
  "message": "Asset registered successfully",
  "assetId": "ASSET-1001"
}
```

The identifier shown is illustrative. The final implementation should generate or validate unique asset identifiers according to the system requirements.

### Validation and Error Handling

- Return `400 Bad Request` when submitted data is invalid.
- Return `404 Not Found` when the requested asset does not exist.
- Return `409 Conflict` when a duplicate identifier or other defined data conflict occurs.
- Return an appropriate authorization error when the user is not permitted to perform the operation.

## 4.3.3 Component 2 — Allocation Management API

**Purpose:** Provides operations for allocating available assets and retrieving allocation information.

### Proposed Interface Definition

| Operation | HTTP Method | Endpoint | Purpose |
|---|---|---|---|
| Allocate asset | POST | `/api/allocations` | Allocates an available asset to an authorized assignee. |
| List allocations | GET | `/api/allocations` | Retrieves allocation records according to access permissions. |
| Get allocation details | GET | `/api/allocations/{allocationId}` | Retrieves details of a specific allocation. |
| Return asset | POST | `/api/allocations/{allocationId}/return` | Records the return of an allocated asset. |

### Example Request — Allocate Asset

```http
POST /api/allocations
Content-Type: application/json
```

```json
{
  "assetId": "ASSET-1001",
  "assigneeId": "USER-100",
  "allocationDate": "2026-10-12"
}
```

The identifiers and date above are illustrative examples, not actual project records.

### Example Success Response

```json
{
  "message": "Asset allocated successfully",
  "allocationId": "ALLOC-2001",
  "assetId": "ASSET-1001",
  "status": "Allocated"
}
```

### Validation and Error Handling

- Return `400 Bad Request` when required fields or values are invalid.
- Return `404 Not Found` when the specified asset or assignee does not exist.
- Return `409 Conflict` when the asset is unavailable or an allocation conflicts with the current asset state.
- Return an appropriate authorization error when the user lacks permission.

## 4.3.4 Common API Design Considerations

The following conventions are proposed for both interfaces:

1. **Data Format:** JSON is used for request and response bodies.
2. **Input Validation:** Required fields, data types, and values should be validated before processing.
3. **Authorization:** Protected operations should verify the caller's permissions.
4. **Consistent Responses:** Success and error responses should follow a consistent structure.
5. **Data Integrity:** Asset allocation and asset status updates should remain consistent.
6. **Secure Communication:** HTTPS should be used in network deployments.
7. **Documentation:** The API documentation should be updated whenever endpoint behaviour or request and response formats change.

The interfaces in this section describe the planned design. They should not be considered implemented or tested until the corresponding application endpoints have been developed and verified.
