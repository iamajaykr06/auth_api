import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY","dev-secret-key")
    DEBUG = False

    DB_HOST =os.getenv("DB_HOST","localhost")
    DB_USER =os.getenv("DB_USER","root")
    DB_PASSWORD =os.getenv("DB_PASSWORD","")
    DB_NAME =os.getenv("DB_NAME","auth_db")

class DevelopmentConfig(BaseConfig):
    DEBUG = True