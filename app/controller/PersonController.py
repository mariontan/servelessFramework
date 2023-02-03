from fastapi import HTTPException, APIRouter

from .BaseController import dynamodb, table
from app.data_store import PersonModel
from app.repository.PersonRepository import PersonRepository
from app.core.PersonService import PersonService
from app.external_gateway import AuthenticationGateway,IntegrationHubGateway

router = APIRouter()
personRepository = PersonRepository(dynamodb, table)
personService = PersonService(personRepository)


@router.post("/person")
async def create_person(person: PersonModel.Person):
    token = await AuthenticationGateway.get_auth_token()
    hub_person_resp = await IntegrationHubGateway.create_person(person,token)
    setattr(person,'person_id',hub_person_resp['entryId'])
    personFields = PersonModel.Person.__fields__.keys()
    for field in personFields:
        if not person.dict().get(field):
            raise HTTPException(
                status_code=422, detail=f"{field.capitalize()} is required")
    await personService.create_person(person)
    return {
        "message": "Person created", 
        "person": person,
        "integrationHub":hub_person_resp
    }


@router.get('/persons')
async def get_persons():
    persons = await personService.get_persons()
    return {"persons": persons}


@router.get("/person/{person_id}")
async def retrieve_person(person_id: str):
    if (not isinstance(person_id, str)):
        raise HTTPException(status_code=422, detail='id must be a string')
    person = await personService.retrieve_person(person_id)
    token = await AuthenticationGateway.get_auth_token()
    hub_person_response = await IntegrationHubGateway.get_person(person_id,token)
    return {
        "person":person,
        "integrationHub":hub_person_response
    }


@router.put("/person/{person_id}")
async def update_person(person_id: str, person: PersonModel.Person):
    await personService.update_person(person_id, person)
    return {"message": "Person updated"}


@router.delete("/person/{person_id}")
async def delete_person(person_id: str):
    await personService.delete_person(person_id)
    return {"message": "Person deleted"}
