import json

def test_create_user(client):
    response = client.post(
        "/users",
        data=json.dumps({
            "email": "test3@example.com",
            "password": "password123"
        }),
        content_type="application/json"
    )
    assert response.status_code == 201

def test_profile_requires_auth(client):
    response = client.get("/users/me")
    assert response.status_code == 401
