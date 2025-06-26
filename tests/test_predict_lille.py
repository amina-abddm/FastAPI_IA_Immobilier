# pour executer les tests ouvrir le terminal : pytest tests/test_predict_lille.py


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_lille():
    response = client.post(
        "/predict/{ville}",
        json={
            "surface_bati": 100,
            "nombre_pieces": 4,
            "type_local": "Appartement",
            "surface_terrain": 0,
            "nombre_lots": 1
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "prix_m2_estime" in data
    assert data["ville_modele"] == "Lille"
    assert isinstance(data["prix_m2_estime"], float)
