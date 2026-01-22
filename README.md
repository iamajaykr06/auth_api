# AUTH_API

A RESTful authentication API built with Flask and JSON Web Tokens (JWT).
The API provides user authentication, protected routes, and secure token-based access.

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

### Get Current User

Returns the authenticated user’s profile information.

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

## Tech Stack

* Python
* Flask
* Flask-JWT-Extended
* MySQL