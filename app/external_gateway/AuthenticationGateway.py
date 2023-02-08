import requests
from .constants import base,appId,appSecret

async def get_auth_token():
    api = "users/login/"
    url = f"{base}{api}?appId={appId}&appSecret={appSecret}&redirectCode=False"
    payload = {
        "username": "fa89f90c-8bf4-4165-9eed-596501da0741",
        "password": "Advice*123"
    }
    response = requests.post(url,json=payload)
    parsed_response = response.json()
    return parsed_response['accessToken']