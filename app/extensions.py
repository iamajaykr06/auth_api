import mysql.connector
from flask_jwt_extended import JWTManager
from flask import current_app

jwt = JWTManager()

def get_db_connection():
    return mysql.connector.connect(
        host = current_app.config["DB_HOST"],
        user = current_app.config["DB_USER"],
        password = current_app.config["DB_PASSWORD"],
        database = current_app.config["DB_NAME"]
    )