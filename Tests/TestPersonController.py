import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
import uuid
@pytest.fixture
def client():
    from ..app.controller import PersonController
    return TestClient(PersonController.router)

def test_create_person(client):
    person = {
        "first_name": "test",
        "last_name": "test",
        "email": "test@test.com",
        "phone": "123456789",
    }
    resp = client.post("/person", json=person)
    assert resp.status_code == 200
    assert resp.json()["person"]["first_name"] == person["first_name"]
    assert resp.json()["person"]["last_name"] == person["last_name"]
    assert resp.json()["person"]["email"] == person["email"]
    assert resp.json()["person"]["phone"] == person["phone"]

def test_get_persons(client):
    resp = client.get("/persons")
    assert resp.status_code == 200
    assert "persons" in resp.json()

def test_retrieve_person(client):
    person_id = str(uuid.uuid4())
    resp = client.get(f"/person/{person_id}")
    assert resp.status_code == 404

def test_update_person(client):
    person_id = str(uuid.uuid4())
    person = {
        "first_name": "test",
        "last_name": "test",
        "email": "test@test.com",
        "phone": "123456789",
    }
    resp = client.put(f"/person/{person_id}", json=person)
    assert resp.status_code == 200
    assert resp.json() == {"message": "Person updated"}

def test_delete_person(client):
    person_id = str(uuid.uuid4())
    resp = client.delete(f"/person/{person_id}")
    assert resp.status_code == 404

def test_delete_person_invalid_uuid(client):
    person_id = "invalid_uuid"
    resp = client.delete(f"/person/{person_id}")
    assert resp.status_code == 422