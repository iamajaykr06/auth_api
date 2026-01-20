from flask import Flask
from .config import DevelopmentConfig
from .extensions import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    jwt.init_app(app)
    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    return app