from app.data_store import PersonModel


class PersonRepository():

    def __init__(self, dynamodb, table):
        self.dynamodb = dynamodb
        self.table = table

    async def create_person(self, person: PersonModel.Person):
        return self.table.put_item(Item=person.dict())

    async def get_persons(self):
        response = self.table.scan()
        persons = response.get("Items")
        return persons

    async def retrieve_person(self, person_id: str):
        response = self.table.get_item(Key={"person_id": person_id})
        person = response.get("Item", {})
        return person

    async def update_person(self, person_id: str, person: PersonModel.Person):
        person = self.table.update_item(Key={"person_id": person_id}, UpdateExpression="set first_name=:fn, last_name=:ln, preferred_name=:pn, dob=:dob, gender=:g, marital_status=:ms, mobile_number=:mn, home_email=:hemail, office_email=:oemail, home_address=:haddr, office_address=:oaddr", ExpressionAttributeValues={
            ":fn": person.first_name, ":ln": person.last_name, ":pn": person.preferred_name, ":dob": person.dob, ":g": person.gender, ":ms": person.marital_status, ":mn": person.mobile_number, ":hemail": person.home_email, ":oemail": person.office_email, ":haddr": person.home_address, ":oaddr": person.office_address}, ReturnValues="UPDATED_NEW")
        return person

    async def delete_person(self, person_id: str):
        self.table.delete_item(Key={"person_id": person_id})
        return person_id
