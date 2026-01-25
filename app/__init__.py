from flask import Flask, send_from_directory
from .config import DevelopmentConfig
from .extensions import jwt
from .utils.errors import register_error_handlers
from .utils.logger import setup_logging
from app.routes.users import users_bp
from app.routes.auth import auth_bp
import os

def create_app():

    setup_logging()

    app = Flask(__name__, static_folder='../frontend/static', static_url_path='/static')
    app.config.from_object(DevelopmentConfig)
    register_error_handlers(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    @app.route("/health")
    def health_check():
        return {"status":"ok"},200

    # Serve frontend HTML files
    @app.route("/")
    def index():
        return send_from_directory(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend'), 'index.html')
    
    @app.route("/index.html")
    def index_html():
        return send_from_directory(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend'), 'index.html')
    
    @app.route("/register.html")
    def register():
        return send_from_directory(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend'), 'register.html')
    
    @app.route("/dashboard.html")
    def dashboard():
        return send_from_directory(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend'), 'dashboard.html')

    return app