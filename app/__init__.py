from flask import Flask
from .config import DevelopmentConfig
from .extensions import jwt
from .utils.errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    jwt.init_app(app)
    register_error_handlers(app)
    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    return app