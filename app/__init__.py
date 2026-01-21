from flask import Flask
from .config import DevelopmentConfig
from .extensions import jwt
from .utils.errors import register_error_handlers
from .utils.logger import setup_logging
from app.routes.users import users_bp

def create_app():

    setup_logging()

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(users_bp)

    jwt.init_app(app)
    register_error_handlers(app)

    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    return app