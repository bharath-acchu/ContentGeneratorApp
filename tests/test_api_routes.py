from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_generate_endpoint_missing_body():
    response = client.post("/generate", json={})
    assert response.status_code == 422

def test_history_endpoint_without_user_id():
    response = client.get("/history")
    assert response.status_code == 422
