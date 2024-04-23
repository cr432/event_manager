from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_user_unauthenticated():
    response = client.get("/users/some_user_id")
    assert response.status_code == 401

def test_update_user_unauthenticated():
    response = client.put("/users/some_user_id", json={})
    assert response.status_code == 401

def test_delete_user_unauthenticated():
    response = client.delete("/users/some_user_id")
    assert response.status_code == 401

def test_create_user_unauthenticated():
    response = client.post("/users/", json={})
    assert response.status_code == 401

def test_list_users_unauthenticated():
    response = client.get("/users/")
    assert response.status_code == 401

def test_register_missing_fields():
    response = client.post("/register/", json={})
    assert response.status_code == 422

def test_register_existing_user():
    response = client.post("/register/", json={"username": "existing_user", "password": "password123"})
    assert response.status_code == 422

def test_login_missing_fields():
    response = client.post("/login/")
    assert response.status_code == 422

def test_login_invalid_credentials():
    response = client.post("/login/", data={"username": "nonexistent_user", "password": "wrong_password"})
    assert response.status_code == 422
