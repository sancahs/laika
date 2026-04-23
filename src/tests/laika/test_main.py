import pytest
from fastapi.testclient import TestClient

from laika.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_status(client):
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"api_status": True, "db_status": False}


def test_status_space_api(client):
    response = client.get("/status/space-api")

    data = response.json()
    assert response.status_code == 200
    assert data["space"] == "Sanca Hackerspace"
