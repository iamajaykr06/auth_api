import mysql.connector
from flask_jwt_extended import JWTManager
from flask import current_app
from app.utils.errors import APIError

jwt = JWTManager()

def get_db_connection():
    """Get database connection with error handling."""
    try:
        return mysql.connector.connect(
            host=current_app.config["DB_HOST"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            database=current_app.config["DB_NAME"],
            autocommit=False
        )
    except mysql.connector.Error as e:
        raise APIError(f"Database connection failed: {str(e)}", 500)

@jwt.unauthorized_loader
def missing_token(error):
    raise APIError("Missing or invalid token", 401)

@jwt.invalid_token_loader
def invalid_token(error):
    raise APIError("Invalid token", 401)

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    raise APIError("Token expired", 401)