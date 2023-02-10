from typing import Optional

from pydantic import BaseModel
import pydantic


class Person(BaseModel):
    person_id: str
    contactDetailId:str
    firstName: str
    lastName: str
    preferredName: str
    dateOfBirth: str
    gender: str
    maritalStatus: str
    mobileNumber: str
    homeEmail: str
    officeEmail: str
    homeAddress: str
    officeAddress: str


class PersonPartial(BaseModel):
    person_id: Optional[str]
    contactDetailId:Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    preferredName: Optional[str]
    dateOfBirth: Optional[str]
    gender: Optional[str]
    maritalStatus: Optional[str]
    mobileNumber: Optional[str]
    homeEmail: Optional[str]
    officeEmail: Optional[str]
    homeAddress: Optional[str]
    officeAddress: Optional[str]
