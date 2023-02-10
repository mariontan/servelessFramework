import requests
from .constants import base
from ..data_store import PersonModel

api = 'hub/api/v1/people/'

async def create_person(person:PersonModel.Person, token):
    url = f"{base}{api}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload={
        "firstName":person.firstName,
        "lastName":person.lastName,
        "userGroup": "Client Group",
        "clientGroupId":"string",
        "userRoles": [
            "primary_client"
        ],
        "preferredName":person.preferredName,
        "dateOfBirth":person.dateOfBirth,
        "gender":person.gender,
        "maritalStatus":person.maritalStatus,
        "practiceId": "2"
    }
    response = requests.post(url,headers=headers,json=payload)
    return response.json()

async def update_person(person:PersonModel.PersonPartial,entryId:str, token):
    url = f"{base}{api}{entryId}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload={
        "userGroup": "Client Group",
        "clientGroupId":"string",
        "userRoles": [
            "primary_client"
        ],
        "practiceId": "2"
    }
    person_dict = person.dict()
    person_dict = {k: v for k, v in person_dict.items() if v is not None}
    updated_values = {f"{key}": value for key, value in person_dict.items()}
    print(type(updated_values))
    print(type(payload))
    print(payload.update(updated_values))
    print(payload)
    # response = requests.post(url,headers=headers,json=payload)
    # return response.json()




async def get_person(entryId:str,token):
    url = f"{base}{api}{entryId}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "practiceId":"2",
        "clientGroupId":"string"
    }
    response = requests.get(url,headers=headers,params=params)
    return response.json()

async def delete_person(entryId:str,token):
    url = f"{base}{api}{entryId}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "practiceId":"2",
        "clientGroupId":"string"
    }
    response = requests.delete(url,headers=headers,params=params)
    return response.json()


