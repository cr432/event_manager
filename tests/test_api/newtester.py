from fastapi.testclient import TestClient
from app.main import app

# Initialize the TestClient with the FastAPI app
client = TestClient(app)

# Tests for successful authentication
def test_successful_authentication():
    response = client.post(
        "/token",
        data={"username": "valid_user", "password": "valid_password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

# Tests for authentication failure due to incorrect username
def test_authentication_failure_incorrect_username():
    response = client.post(
        "/token",
        data={"username": "invalid_user", "password": "valid_password"}
    )
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Incorrect username or password"

# Tests for authentication failure due to incorrect password
def test_authentication_failure_incorrect_password():
    response = client.post(
        "/token",
        data={"username": "valid_user", "password": "invalid_password"}
    )
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Incorrect username or password"
