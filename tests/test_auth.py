import json

def test_login_success(client, db_setup, test_user):
    response = client.post(
        "/auth/login",
        data=json.dumps({
            "email": test_user["email"],
            "password": test_user["password"]
        }),
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "access_token" in response.get_json()


def test_login_invalid_credentials(client, db_setup):
    response = client.post(
        "/auth/login",
        data=json.dumps({
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }),
        content_type="application/json"
    )
    assert response.status_code == 401
    assert "error" in response.get_json()


def test_login_missing_fields(client):
    response = client.post(
        "/auth/login",
        data=json.dumps({
            "email": "test@example.com"
        }),
        content_type="application/json"
    )
    assert response.status_code == 400
