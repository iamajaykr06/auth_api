from flask import Blueprint, request
from app.services.user_service import UserService
from app.utils.errors import APIError
from app.models.user import UserModel
from flask_jwt_extended import jwt_required,get_jwt_identity,get_jwt

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        raise APIError("Invalid JSON body", 400)

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise APIError("Email and password required", 400)

    if "@" not in email:
        raise APIError("Invalid email format", 400)

    if len(password) < 8:
        raise APIError("Password too short", 400)

    UserService.create_user(email, password)

    return {"message": "User created"}, 201

@users_bp.route("/me", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = UserModel.find_by_id(user_id)

    if not user:
        raise APIError("User not found", 404)

    return {
        "id": user["id"],
        "email": user["email"],
        "created_at": user["created_at"]
    }, 200
