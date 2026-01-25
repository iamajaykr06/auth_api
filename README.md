# SecureAuth

A full-stack authentication application with a modern web frontend and RESTful API backend built with Flask and JSON Web Tokens (JWT). The application provides user registration, authentication, protected routes, and secure token-based access with a beautiful, responsive user interface.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd secureauth
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
   The application will be available at `http://localhost:5000`
   - Frontend: `http://localhost:5000` (Login page)
   - API endpoints: `http://localhost:5000/auth/*` and `http://localhost:5000/users/*`

---

## Quick Start Guide

### Using the Web Interface

1. **Open your browser** and navigate to `http://localhost:5000`

2. **Create an account:**
   - Click on "Sign up" link on the login page
   - Enter your email and password (minimum 8 characters)
   - Confirm your password
   - Click "Create Account"
   - You'll be redirected to the login page

3. **Login:**
   - Enter your email and password
   - Click "Login"
   - You'll be redirected to your dashboard

4. **View your profile:**
   - The dashboard displays your user ID, email, and account creation date
   - Click "Logout" to sign out

### Using the API Directly

You can also interact with the API directly using tools like `curl` or Postman:

**Register a user:**
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

**Login:**
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

**Get profile (replace TOKEN with your access token):**
```bash
curl -X GET http://localhost:5000/users/me \
  -H "Authorization: Bearer TOKEN"
```

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

---

## Frontend

SecureAuth includes a modern, responsive web frontend built with vanilla HTML, CSS, and JavaScript. The frontend provides a seamless user experience for authentication and account management.

### Frontend Pages

#### Login Page (`/` or `/index.html`)
- User authentication interface
- Email and password input with validation
- Error handling and user feedback
- Automatic redirect to dashboard on successful login

#### Registration Page (`/register.html`)
- New user account creation
- Password confirmation
- Real-time validation (email format, password length)
- Success message and automatic redirect to login

#### Dashboard (`/dashboard.html`)
- Protected user profile page
- Displays user information (ID, email, account creation date)
- Logout functionality
- Automatic redirect to login if not authenticated

### Frontend Features

- **Modern UI Design**: Clean, professional interface with gradient backgrounds and smooth animations
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Token Management**: Automatic JWT token storage and management using localStorage
- **Protected Routes**: Automatic authentication checks and redirects
- **Error Handling**: User-friendly error messages for all API interactions
- **Loading States**: Visual feedback during API requests
- **Form Validation**: Client-side validation before API calls

### Frontend Architecture

The frontend is organized into modular JavaScript files:

- `auth.js`: Core authentication utilities, API client, and token management
- `login.js`: Login page functionality
- `register.js`: Registration page functionality
- `dashboard.js`: Dashboard page functionality

All styling is centralized in `style.css` with CSS variables for easy theming.

---

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

### Backend
* Python 3.x
* Flask 3.1.2
* Flask-JWT-Extended 4.7.1
* MySQL (mysql-connector-python 9.5.0)
* Werkzeug 3.1.5 (for password hashing)
* pytest 8.3.3 (for testing)
* pytest-flask 1.3.0 (for Flask test fixtures)

### Frontend
* HTML5
* CSS3 (with CSS Variables for theming)
* Vanilla JavaScript (ES6+)
* Fetch API for HTTP requests
* LocalStorage for token management

---

## Project Structure

```
secureauth/
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
│       └── security.py      # Password hashing utilities
├── frontend/
│   ├── index.html           # Login page
│   ├── register.html        # Registration page
│   ├── dashboard.html       # User dashboard
│   └── static/
│       ├── css/
│       │   └── style.css    # Main stylesheet
│       └── js/
│           ├── auth.js      # Authentication utilities
│           ├── login.js     # Login page logic
│           ├── register.js # Registration page logic
│           └── dashboard.js # Dashboard page logic
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── test_auth.py         # Authentication tests
│   └── test_users.py        # User management tests
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```