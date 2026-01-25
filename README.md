# AUTH_API

A RESTful authentication API built with Flask and JSON Web Tokens (JWT).
The API provides user authentication, protected routes, and secure token-based access.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd auth_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your-database-password
   DB_NAME=auth_db
   JWT_SECRET_KEY=your-jwt-secret-key-here
   ```

6. **Set up the database** (see Database Schema section below)

7. **Run the application**
   ```bash
   python run.py
   ```
   The API will be available at `http://localhost:5000`

---

## Authentication

Authentication is handled using JSON Web Tokens (JWT).

Users authenticate via the `/auth/login` endpoint.  
On successful login, the server returns a signed JWT access token.  
This token must be included in subsequent requests to protected endpoints using the
`Authorization: Bearer <token>` header.

JWT access tokens are short-lived and expire after 1 hour.  
Expired tokens require re-authentication (refresh tokens are not implemented).

---

## API Endpoints

### Register User

**POST** `/users`

Creates a new user account.

**Request Body**
```json
{
  "email": "user@example.com",
  "password": "secret123"
}
```

**Validation:**
- Email must be a valid email format
- Password must be at least 8 characters long

**Response:**
```json
{
  "message": "User created"
}
```
**Status Code:** 201

**Error Responses:**
- 400: Invalid input (missing fields, invalid email format, password too short)
- 409: User already exists

---

### Login

**POST** `/auth/login`

Authenticates a user and returns a JWT access token.

**Request Body**
```json
{
  "email": "user@example.com",
  "password": "secret123"
}
```
**Response:**
```json
{
  "access_token": "<jwt-token>"
}
```
**Status Code:** 200

**Error Responses:**
- 400: Missing email or password
- 401: Invalid credentials

---

### Get Current User

Returns the authenticated user's profile information.

**GET** `/users/me`

**Headers:**
```
Authorization: Bearer <jwt-token>
```
**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "created_at": "2026-01-21T10:30:00"
}
```
**Status Code:** 200

**Error Responses:**
- 401: Missing or invalid token
- 404: User not found

---

### Health Check

**GET** `/health`

Returns the health status of the API.

**Response:**
```json
{
  "status": "ok"
}
```
**Status Code:** 200

## Database Schema

The application uses a MySQL database with a single `users` table.

**Step 1: Create the database manually**
``` 
CREATE DATABASE auth_db;
USE auth_db;
```

**Step 2: Create `users` table**
```
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Security Notes

* Passwords are never stored or returned in plain text.
* Passwords are securely hashed before storage.
* JWT access tokens are required for protected routes.
* Sensitive fields such as password hashes and tokens are never exposed in API responses.

## Testing

Run the test suite using pytest:

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

**Note:** Make sure you have a test database configured. The tests use `auth_db_test` by default (can be configured in `tests/conftest.py`).

---

## Tech Stack

* Python 3.x
* Flask 3.1.2
* Flask-JWT-Extended 4.7.1
* MySQL (mysql-connector-python 9.5.0)
* Werkzeug 3.1.5 (for password hashing)
* pytest 8.3.3 (for testing)
* pytest-flask 1.3.0 (for Flask test fixtures)

---

## Project Structure

```
auth_api/
├── app/
│   ├── __init__.py          # Application factory
│   ├── config.py            # Configuration settings
│   ├── extensions.py        # Flask extensions (JWT, DB)
│   ├── models/
│   │   └── user.py          # User data model
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   └── users.py         # User management routes
│   ├── services/
│   │   ├── auth_service.py  # Authentication business logic
│   │   └── user_service.py  # User management business logic
│   └── utils/
│       ├── errors.py        # Error handling
│       ├── logger.py        # Logging configuration
│       └── security.py     # Password hashing utilities
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── test_auth.py         # Authentication tests
│   └── test_users.py      # User management tests
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```