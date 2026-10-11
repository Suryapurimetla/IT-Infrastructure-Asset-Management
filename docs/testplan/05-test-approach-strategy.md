# 5. Test Approach / Strategy

## 5.1 Test Levels

Testing will be performed at the following levels, depending on the availability of the implementation and test environment.

### Unit Testing

Individual functions and validation rules will be tested independently where unit tests are available.

### Integration Testing

Interactions between application modules and the data store will be tested to verify that information is exchanged and processed correctly.

### System Testing

The complete application workflows will be tested against the approved Software Requirements Specification (SRS).

### Acceptance Testing

The team will verify whether the implemented features satisfy the agreed acceptance criteria.

## 5.2 Test Types

### Functional Testing

Verify that each implemented feature produces the expected result.

### Validation Testing

Check mandatory fields, data formats, unique asset identifiers and date values according to the approved requirements.

### Regression Testing

Repeat relevant tests after changes to check that previously working features have not been affected.

### Usability Testing

Check whether users can complete common asset management tasks clearly and consistently.

### Performance Testing

Measure response times for important operations against measurable performance requirements defined in the SRS.

### Security Testing

Check access permissions, input handling and protection against unauthorized actions where the corresponding controls are implemented.

## 5.3 Test Design

Test cases will cover normal inputs, invalid inputs and important boundary conditions. Each test case will include a unique identifier, preconditions, test steps, expected result, actual result, status and related SRS requirement ID.

## 5.4 Entry Criteria

Testing may begin when:

- The feature's expected behaviour is documented.
- The required application or component is available.
- The test environment and necessary test data are available.
- The corresponding requirement has an agreed identifier.

## 5.5 Exit Criteria

Testing can be considered complete for the planned scope when:

- Planned test cases have recorded execution statuses.
- Critical and high-severity defects are resolved or formally documented for review.
- Failed and blocked tests have explanations.
- Requirement coverage and remaining risks are reported.
- The team has reviewed the test summary.

## 5.1 Security Validation

Security validation will cover the following checks where the relevant controls are implemented:

1. Verify that only authorized users can access protected functions.
2. Verify that users cannot perform operations outside their permissions.
3. Verify that invalid input is handled safely.
4. Check that error messages do not expose unnecessary internal details.
5. Verify that unauthorized changes to asset records are prevented.
6. Check authentication and session handling if login functionality exists.
7. Verify relevant security event logging where logging is implemented.
8. Check that sensitive configuration values are not exposed.

Security test results will be recorded as Pass, Fail, Blocked or Not Run. Controls that are not implemented will be documented as gaps rather than marked as passed.
