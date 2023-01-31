from fastapi import HTTPException, APIRouter

from .BaseController import dynamodb, table
from data_store import PersonModel
from repository.PersonRepository import PersonRepository
from core.PersonService import PersonService

router = APIRouter()
personRepository = PersonRepository(dynamodb, table)
personService = PersonService(personRepository)


@router.post("/person")
async def create_person(person: PersonModel.Person):
    personFields = PersonModel.Person.__fields__.keys()
    for field in personFields:
        if not person.dict().get(field):
            raise HTTPException(
                status_code=400, detail=f"{field.capitalize()} is required")
    await personService.create_person(person)
    return {"message": "Person created", "person": person}


@router.get('/persons')
async def get_persons():
    persons = await personService.get_persons()
    return {"persons": persons}


@router.get("/person/{person_id}")
async def retrieve_person(person_id: str):
    if (not isinstance(person_id, str)):
        raise HTTPException(status_code=402, detail='id must be a string')
    person = await personService.retrieve_person(person_id)
    return person


@router.put("/person/{person_id}")
async def update_person(person_id: str, person: PersonModel.Person):
    await personService.update_person(person_id, person)
    return {"message": "Person updated"}


@router.delete("/person/{person_id}")
async def delete_person(person_id: str):
    await personService.delete_person(person_id)
    return {"message": "Person deleted"}