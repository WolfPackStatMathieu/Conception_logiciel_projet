from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_all_demandes():
    response = client.get("/demande/all")
    assert response.status_code == 200
