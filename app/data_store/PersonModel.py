from typing import Optional

from pydantic import BaseModel
import pydantic


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

# class AllOptional(pydantic.main.ModelMetaclass):
#     def __new__(self, name, bases, namespaces, **kwargs):
#         annotations = namespaces.get('__annotations__', {})
#         for base in bases:
#             annotations.update(base.__annotations__)
#         for field in annotations:
#             if not field.startswith('__'):
#                 annotations[field] = Optional[annotations[field]]
#         namespaces['__annotations__'] = annotations
#         return super().__new__(self, name, bases, namespaces, **kwargs)

    
# class PersonPartial(Person, metaClass =AllOptional ):
#     pass
class PersonPartial(BaseModel):
    person_id: Optional[str]
    contact_detail_id:Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    preferred_name: Optional[str]
    dob: Optional[str]
    gender: Optional[str]
    marital_status: Optional[str]
    mobile_number: Optional[str]
    home_email: Optional[str]
    office_email: Optional[str]
    home_address: Optional[str]
    office_address: Optional[str]
