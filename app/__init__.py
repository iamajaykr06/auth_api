from flask import Flask
from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    return app