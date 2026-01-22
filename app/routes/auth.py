from flask import Blueprint, request
from app.services.auth_service import AuthService
from app.utils.errors import APIError

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        raise APIError("Invalid JSON body", 400)

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise APIError("Email and password required", 400)

    token = AuthService.login(email, password)

    return {"access_token": token}, 200
