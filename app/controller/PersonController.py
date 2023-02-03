from fastapi import HTTPException, APIRouter

from .BaseController import dynamodb, table
from app.data_store import PersonModel
from app.repository.PersonRepository import PersonRepository
from app.core.PersonService import PersonService
from app.external_gateway import AuthenticationGateway,IntegrationHubPersonGateway,IntegrationHubContactGateway
from app.utils import utils
router = APIRouter()
personRepository = PersonRepository(dynamodb, table)
personService = PersonService(personRepository)


@router.post("/person")
async def create_person(person: PersonModel.Person):
    token = await AuthenticationGateway.get_auth_token()
    hub_person_resp = await IntegrationHubPersonGateway.create_person(person,token)
    setattr(person,'person_id',hub_person_resp['entryId'])
    hub_contact_resp = await IntegrationHubContactGateway.create_contact_detail(person,token)
    setattr(person,'contact_detail_id',hub_contact_resp['entryId'])
    await personService.create_person(person)
    return {
        "person": person,
        "integrationHubPerson":hub_person_resp,
        "integrationHubContact":hub_contact_resp
    }


@router.get('/persons')
async def get_persons():
    persons = await personService.get_persons()
    return {"persons": persons}


@router.get("/person/{person_id}")
async def retrieve_person(person_id: str):
    if (not utils.is_valid_uuid(person_id)):
        raise HTTPException(status_code=422, detail='id must be a uuid')
    person = await personService.retrieve_person(person_id)
    if( not person):
        raise HTTPException(status_code=404, detail='entry deleted')
    token = await AuthenticationGateway.get_auth_token()
    hub_person_response = await IntegrationHubPersonGateway.get_person(person_id,token)
    hub_contact_response = await IntegrationHubContactGateway.get_contact_detail(person['contact_detail_id'],token)
    return {
        "person":person,
        "integrationHubPerson":hub_person_response,
        "integrationHubContact":hub_contact_response
    }


@router.put("/person/{person_id}")
async def update_person(person_id: str, person: PersonModel.Person):
    await personService.update_person(person_id, person)
    return {"message": "Person updated"}


@router.delete("/person/{person_id}")
async def delete_person(person_id: str):
    if (not utils.is_valid_uuid(person_id)):
        raise HTTPException(status_code=422, detail='id must be a uuid')
    person = await personService.retrieve_person(person_id)
    await personService.delete_person(person_id)
    token = await AuthenticationGateway.get_auth_token()
    hub_person_response = await IntegrationHubPersonGateway.delete_person(person_id,token)
    hub_contact_response = await IntegrationHubContactGateway.delete_contact_detail(person['contact_detail_id'],token)
    return {
        "message": f"Person with id {person_id} deleted",
        "integrationHubPerson":hub_person_response,
        "integrationHubContact":hub_contact_response
    }
