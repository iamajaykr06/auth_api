import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY","dev-secret-key")
    DEBUG = False

    DB_HOST =os.getenv("DB_HOST","localhost")
    DB_USER =os.getenv("DB_USER","root")
    DB_PASSWORD =os.getenv("DB_PASSWORD","")
    DB_NAME =os.getenv("DB_NAME","auth_db")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-dev-secret")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour

class DevelopmentConfig(BaseConfig):
    DEBUG = True