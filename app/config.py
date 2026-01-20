import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY","dev-secret-key")
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True