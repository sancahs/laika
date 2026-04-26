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


def test_open_hackerspace(client):
    response = client.post("/v1/hackerspace/open")

    data = response.json()
    assert response.status_code == 200
    assert data == {"is_open": True, "status": "open"}


def test_close_hackerspace(client):
    response = client.post("/v1/hackerspace/close")

    data = response.json()
    assert response.status_code == 200
    assert data == {"is_open": False, "status": "closed"}


def test_get_hackerspace_open_status_open(client, db_session, hs_is_open):
    hs_is_open.value = "open"
    db_session.commit()

    response = client.get("/v1/hackerspace/is-open")

    data = response.json()
    assert response.status_code == 200
    assert data == {"is_open": True, "status": "open"}


def test_get_hackerspace_open_status_closed(client, db_session, hs_is_open):
    hs_is_open.value = "closed"
    db_session.commit()

    response = client.get("/v1/hackerspace/is-open")

    data = response.json()
    assert response.status_code == 200
    assert data == {"is_open": False, "status": "closed"}
