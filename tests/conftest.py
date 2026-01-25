import pytest
from app import create_app
from app.extensions import get_db_connection


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['DB_NAME'] = 'auth_db_test'  # Use test database
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def db_setup(app):
    """Set up test database."""
    with app.app_context():
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY AUTO_INCREMENT,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        yield
        
        # Cleanup: drop table after tests
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        conn.commit()
        cursor.close()
        conn.close()


@pytest.fixture
def test_user(app, db_setup):
    """Create a test user for authentication tests."""
    with app.app_context():
        from app.services.user_service import UserService
        UserService.create_user("success@example.com", "password123")
    return {"email": "success@example.com", "password": "password123"}
