import json

def test_login_success(client):
    response = client.post(
        "/auth/login",
        data=json.dumps({
            "email": "success@example.com",
            "password": "password123"
        }),
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "access_token" in response.get_json()
