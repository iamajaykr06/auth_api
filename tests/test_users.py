import json
from flask_jwt_extended import create_access_token

def test_create_user(client, db_setup):
    response = client.post(
        "/users",
        data=json.dumps({
            "email": "test3@example.com",
            "password": "password123"
        }),
        content_type="application/json"
    )
    assert response.status_code == 201
    assert "message" in response.get_json()


def test_create_user_duplicate_email(client, db_setup):
    # Create first user
    client.post(
        "/users",
        data=json.dumps({
            "email": "duplicate@example.com",
            "password": "password123"
        }),
        content_type="application/json"
    )
    
    # Try to create duplicate
    response = client.post(
        "/users",
        data=json.dumps({
            "email": "duplicate@example.com",
            "password": "password123"
        }),
        content_type="application/json"
    )
    assert response.status_code == 409


def test_create_user_invalid_email(client, db_setup):
    response = client.post(
        "/users",
        data=json.dumps({
            "email": "invalid-email",
            "password": "password123"
        }),
        content_type="application/json"
    )
    assert response.status_code == 400


def test_create_user_short_password(client, db_setup):
    response = client.post(
        "/users",
        data=json.dumps({
            "email": "test@example.com",
            "password": "short"
        }),
        content_type="application/json"
    )
    assert response.status_code == 400


def test_profile_requires_auth(client):
    response = client.get("/users/me")
    assert response.status_code == 401


def test_get_profile_success(client, db_setup, test_user):
    from app import create_app
    app = create_app()
    app.config['TESTING'] = True
    
    with app.app_context():
        from app.models.user import UserModel
        user = UserModel.find_by_email(test_user["email"])
        token = create_access_token(identity=str(user["id"]))
    
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data
    assert "email" in data
    assert "created_at" in data
    assert data["email"] == test_user["email"]
