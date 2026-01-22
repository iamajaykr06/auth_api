from flask_jwt_extended import create_access_token
from app.models.user import UserModel
from app.utils.security import verify_password
from app.utils.errors import APIError

class AuthService:

    @staticmethod
    def login(email, password):
        user = UserModel.find_by_email(email)

        if not user:
            raise APIError("Invalid credentials", 401)

        if not verify_password(password, user["password_hash"]):
            raise APIError("Invalid credentials", 401)

        token = create_access_token(identity=str(user["id"]))
        return token
