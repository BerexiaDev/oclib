# OC Global Library

This repository serves as a centralized collection of reusable code components for various microservices in OC Platform. It includes key functionality such as authentication with Keycloak, PostgreSQL data models, shared DTOs, utilities, exception handling, advanced filtering logic, and more. This library is designed to improve consistency, reduce code duplication, and streamline development across the applications.

## Features

### 1. Authentication with Keycloak

- **Keycloak Decorator**: A decorator that handles authentication using Keycloak, enabling secure access control for your services.
- **Usage**: Apply this decorator to endpoints in your Flask applications to enforce authentication with Keycloak.

### 2. PostgreSQL Data Models

- Centralized data models for PostgreSQL are defined using SQLAlchemy.
- **Usage**: These models can be easily imported and used across services that interact with a PostgreSQL database.

### 3. Shared DTO (Data Transfer Object) Utilities

- Includes various shared DTOs for consistent data formatting and validation across services.
- **Usage**: Import the required DTOs for uniform data exchange between your backend services.

### 4. Shared Exceptions

- **Custom Exceptions**: Define common exceptions like `AlreadyExistsError`, `NotFoundError`, and more.
- **Usage**: These exceptions can be used across microservices to handle errors uniformly.

### 5. Advanced Filter Logic

- **Advanced Filters**: Includes reusable logic for filtering data using complex criteria (e.g., multi-criteria search).
- **Usage**: Import the filter classes into your services to simplify the implementation of advanced filtering.

### 6. Shared Paginator Class

- Provides pagination functionality for listing resources in a scalable way.
- **Usage**: Integrate this paginator in services where large datasets are returned to ensure efficient data navigation.

### 7. Shared Utility Functions

- Common utility functions like `current_year()`, `date_now()`, and more are provided.
- **Usage**: Import these functions as needed for consistent date and time handling across services.

## Installation

To install this shared library into your project, follow these steps:

1. Add this repository to your requirments file:
   ```bash
   oc_lib@git+https://github.com/BerexiaDev/oclib.git@main
   ```
