from ..data_store import PersonModel


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

    async def update_person(self, person_id: str, person: PersonModel.PersonPartial):
        personDict = person.dict()
        personDict = {k: v for k, v in personDict.items() if v is not None}
        update_expression  = "SET " + ", ".join([f"{key} = :{key}" for key in list(personDict.keys())])
        expression_attribute_values = {f":{key}": value for key, value in personDict.items()}
        person = self.table.update_item(
            Key={
                "person_id": person_id
            }, 
            UpdateExpression=update_expression, 
            ExpressionAttributeValues=expression_attribute_values, 
            ReturnValues="UPDATED_NEW")
        return person

    async def delete_person(self, person_id: str):
        self.table.delete_item(Key={"person_id": person_id})
        return person_id
