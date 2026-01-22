from flask import Flask
from .config import DevelopmentConfig
from .extensions import jwt
from .utils.errors import register_error_handlers
from .utils.logger import setup_logging
from app.routes.users import users_bp
from app.routes.auth import auth_bp

def create_app():

    setup_logging()

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    register_error_handlers(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    return app