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
    "firstName":"First",
    "lastName":"Bean",
    "preferredName":"Green T",
    "dateOfBirth":"2023-02-02",
    "gender":"Male",
    "maritalStatus":"Single",
    "mobileNumber":"09335556677",
    "homeEmail":"Beanemail",
    "officeEmail":"officeemail",
    "homeAddress":"hi address",
    "officeAddress":"office"
}
    resp = client.post("/person", json=person)
    assert resp.status_code == 200
    assert resp.json()["person"]["firstName"] == person["firstName"]
    assert resp.json()["person"]["lastName"] == person["lastName"]
    assert resp.json()["person"]["homeEmail"] == person["homeEmail"]
    assert resp.json()["person"]["mobileNumber"] == person["mobileNumber"]

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
        "firstName": "test",
        "lastName": "test",
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