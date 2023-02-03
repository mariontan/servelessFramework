import requests
from .constants import base
from app.data_store import PersonModel

api = 'hub/api/v1/contact-details/'

async def create_contact_detail(person: PersonModel.Person,token):
    url = f"{base}{api}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload ={
        "ownerId": person.person_id,
        "ownerType": "People",
        "contactType": "Mobile",
        "detail": person.mobile_number,
        "isPreferred": True,
        "xplanIndex": "string"
    }
    response = requests.post(url,headers=headers,json=payload)
    return response.json()

async def get_contact_detail(entryId:str,token):
    url = f"{base}{api}{entryId}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url,headers=headers)
    return response.json()