from app.models.users import UserModel
from app.utils.security import hash_password
from app.utils.errors import APIError

class UserService:

    @staticmethod
    def create_user(email, password):
        existing_user = UserModel.find_by_email(email)
        if existing_user:
            raise APIError("User already exists", 409)

        password_hash = hash_password(password)
        UserModel.create(email, password_hash)
