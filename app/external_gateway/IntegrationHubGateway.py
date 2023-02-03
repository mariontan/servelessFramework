import requests
from .constants import base
from app.data_store import PersonModel

async def create_person(person:PersonModel.Person, token):
    api = 'hub/api/v1/people/'
    url = f"{base}{api}"
    headers = {
    "Authorization": f"Bearer {token}"
}
    payload={
        "firstName":person.first_name,
        "lastName":person.last_name,
        "userGroup": "Client Group",
        "clientGroupId":"string",
        "userRoles": [
            "primary_client"
        ],
        "preferredName":person.preferred_name,
        "dateOfBirth":person.dob,
        "gender":person.gender,
        "maritalStatus":person.marital_status,
        "practiceId": "2"
    }
    response = requests.post(url,headers=headers,json=payload)
    return response.json()