from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)

def test_scan_item():
    response = client.post("/scan/A")
    assert response.status_code == 200
    assert response.json() == {'message': 'Scanned item: A successful!'}

def test_get_total():
    response = client.get("/total")
    assert response.status_code == 200
    assert "total_price" in response.json()
