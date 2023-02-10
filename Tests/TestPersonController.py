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
    "person_id":"5",
    "contactDetailId":"5",
    "first_name":"First",
    "last_name":"Bean",
    "preferred_name":"Green T",
    "dob":"2023-02-02",
    "gender":"Male",
    "marital_status":"Single",
    "mobile_number":"09335556677",
    "home_email":"Beanemail",
    "office_email":"officeemail",
    "home_address":"hi address",
    "office_address":"office"
}
    resp = client.post("/person", json=person)
    assert resp.status_code == 200
    assert resp.json()["person"]["first_name"] == person["first_name"]
    assert resp.json()["person"]["last_name"] == person["last_name"]
    assert resp.json()["person"]["home_email"] == person["home_email"]
    assert resp.json()["person"]["mobile_number"] == person["mobile_number"]

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
    print('!!!!!!!!',resp.status_code)
    assert resp.status_code == 422