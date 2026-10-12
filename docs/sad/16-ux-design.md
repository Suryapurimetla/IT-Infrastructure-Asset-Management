# 4.5 UX Design

## 4.5.1 Overview

The user experience (UX) design of the IT Infrastructure & Asset Management System aims to make asset management operations straightforward, consistent, and efficient. The interface should help authorized users access relevant information and complete common tasks with minimal confusion.

The proposed interface will prioritize clarity, ease of navigation, readable information, and consistent feedback.

## 4.5.2 User Interface Principles

The following principles will guide the interface design:

1. **Simplicity:** Present essential information and actions without unnecessary complexity.
2. **Consistency:** Use consistent layouts, labels, buttons, and navigation patterns across screens.
3. **Readability:** Use clear text, appropriate spacing, and distinguishable headings.
4. **Feedback:** Inform users when an operation succeeds, fails, or requires additional input.
5. **Error Prevention:** Validate input and identify missing or incorrect information before submitting operations where possible.
6. **Accessibility:** Use readable text, clear labels, sufficient contrast, and keyboard-accessible controls where supported.
7. **Responsive Layout:** Aim to support common desktop and mobile screen sizes if responsive web design is included in the implementation.

## 4.5.3 Proposed Screens

The system may include the following screens, depending on the final implementation scope.

| Screen | Purpose | Main Elements |
|---|---|---|
| Login Screen | Allows users to authenticate, if authentication is implemented. | Username or email field, password field, and sign-in action. |
| Dashboard | Provides an overview of asset information. | Asset counts, availability information, and upcoming maintenance or expiry items where supported. |
| Asset List | Displays existing asset records. | Search field, filters, asset table, and view or edit actions according to permissions. |
| Asset Registration | Allows authorized users to register assets. | Asset name, category, identifier, serial number, status, and other required fields. |
| Asset Details | Displays information about a selected asset. | Asset attributes, status, allocation information, and related records where available. |
| Allocation Screen | Supports asset allocation and return operations. | Asset selection, assignee details, allocation date, and return action where applicable. |
| Maintenance Screen | Supports maintenance record management. | Asset reference, maintenance description, date, and maintenance status. |
| License and Warranty Screen | Displays and manages license and warranty information. | License or warranty details and relevant expiry dates. |

## 4.5.4 Navigation and User Workflow

The proposed navigation should allow users to move between major asset management functions without unnecessary steps.

A typical workflow is:

1. The user opens the application and authenticates if required.
2. The user navigates to the asset list or dashboard.
3. The user selects an operation such as registering, searching, or updating an asset.
4. The system presents the relevant form or information.
5. The user submits the operation.
6. The system displays a success message or a clear explanation of any error.

Access to functions should depend on the permissions defined in the final security design.

## 4.5.5 Forms and Validation Feedback

Forms should use descriptive field labels and indicate required fields clearly. Validation messages should identify the problem and explain how the user can correct it.

For example:
- A missing asset name should trigger a required-field message.
- An invalid date should trigger a date-format or date-value message.
- A duplicate asset identifier should produce an appropriate conflict message.
- An unavailable asset should not be confirmed as successfully allocated.

Validation should be performed in the application logic even when client-side validation is also provided.

## 4.5.6 UX Design Validation

The interface should be reviewed to determine whether users can complete common operations correctly and understand system feedback.

Potential usability checks include:
- Finding an existing asset.
- Registering a new asset.
- Updating asset information.
- Allocating an available asset.
- Viewing maintenance or expiry information where implemented.
- Understanding validation and error messages.

These checks should be included in the test plan as appropriate. The screens and workflows described here are proposed designs and should be updated to reflect the actual interface developed by the team.
