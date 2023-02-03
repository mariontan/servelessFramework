from pydantic import BaseModel


class Person(BaseModel):
    person_id: str
    contact_detail_id:str
    first_name: str
    last_name: str
    preferred_name: str
    dob: str
    gender: str
    marital_status: str
    mobile_number: str
    home_email: str
    office_email: str
    home_address: str
    office_address: str
