from pydantic import BaseModel , Field, field_validator, ConfigDict, EmailStr
import re
from typing import Optional , TypeVar

class EmployeeCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra = "forbid")

    name : str = Field(min_length=3, max_length=50, description="Employee Full Name")
    email : EmailStr
    phone_number : str 
    age : int = Field(ge=18,le=60)
    salary : int = Field(gt=0)

    @field_validator("phone_number")
    @classmethod
    def phone_validator(cls,value):
        pattern = r"(?:\+?91)?[6-9]\d{9}"
        # pattern = r"\d{10}"
        if not re.fullmatch(pattern , value):
            raise ValueError("Please provide valid phone number")
        return value

    @field_validator('name')
    @classmethod
    def name_validator(self,value):
        if not value.replace(" ","").isalpha():
            raise ValueError
        return value

    
class EmployeeUpdate(BaseModel):
    model_config = Optional(ConfigDict(str_strip_whitespace=True, extra = "forbid"))

    name : str = Optional(Field(min_length=3, max_length=50, description="Employee Full Name"))
    email : str= Optional(EmailStr)
    phone_number: str = Optional(str) 
    age : int = Optional(Field(ge=18,le=60))
    salary : int = Optional(Field(gt=0))

    @field_validator("phone_number")
    @classmethod
    def phone_validator(cls,value):
        pattern = r"(?:\+?91)?[6-9]\d{9}"
        # pattern = r"\d{10}"
        if not re.fullmatch(pattern , value):
            raise ValueError("Please provide valid phone number")
        return value

    @field_validator('name')
    @classmethod
    def name_validator(self,value):
        if not value.replace(" ","").isalpha():
            raise ValueError
        return value

class EmployeeResponse(BaseModel):
    id : int
    name : str
    email : str
    age : int
    salary : float

    model_config = ConfigDict(from_attributes=True)

#from attributes = True allows pydantic to build the response model from object attributes
#SQLALchemy employee = pydantic response model -> JSON 