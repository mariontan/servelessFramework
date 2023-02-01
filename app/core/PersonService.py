from app.data_store import PersonModel


class PersonService():
    def __init__(self, personRepository):
        self.personRepository = personRepository

    async def create_person(self, person: PersonModel.Person):
        await self.personRepository.create_person(person)
        return {"message": "Person created", "person": person}

    async def get_persons(self):
        persons = await self.personRepository.get_persons()
        return {"persons": persons}

    async def retrieve_person(self, person_id: str):
        person = await self.personRepository.retrieve_person(person_id)
        return person

    async def update_person(self, person_id: str, person: PersonModel.Person):
        await self.personRepository.update_person(person_id, person)
        return {"message": "Person updated"}

    async def delete_person(self, person_id: str):
        await self.personRepository.delete_person(person_id)
        return {"message": "Person deleted"}
