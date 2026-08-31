from pydantic import BaseModel , Field, field_validator, ConfigDict, EmailStr
import re

#employee schema - validation -> skills , name , email, department , number , salary , age, password ,address.

#nested pydantic model
class Address(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra = "forbid")
    city:str = Field(max_length=30)
    state:str = Field(max_length=30)
    pincode:str = Field(min_length=6, max_length=6)

class Skills(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra = "forbid")

    programming_language: str = Field(max_length=20)
    experience : int = Field(gt=0, description="Experience in years")

class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra = "forbid")

    name : str = Field(min_length=3, max_length=50, description="Employee Full Name")
    email : EmailStr
    phone_number : str 
    age : int = Field(ge=18,le=60)
    department : str = Field(max_digits=50, description="Please fill your department name")
    salary : int = Field(gt=0)
    address : Address 
    skills: Skills
    is_active: bool = Field(default=True)

    @field_validator("phone_number")
    @classmethod
    def phone_validator(cls,value):
        pattern = r"(?:\+?91)?[6-9]\d{9}"
        # pattern = r"\d{10}"
        if not re.fullmatch(pattern , value):
            raise ValueError("Please provide valid phone number")
        return value

#ge = greater equal 
#le= less then equal 
#gt = geater than 
#lt = less than

#validators : use for the custom validation or transformation of data
# @field_validator('name')
# @classmethod
# def validate_name(cls, value):
#     value = value.strip()

#     if len(value) < 2:
#         raise ValueError("Name must be at least 2")

#     return value



# print(UserCreate.model_json_schema())
#ASDFGHJLK@GMAIL.COM
#asdfghjkl@gmail.com

#field: predefined validation rules
#validator: custom validation rules

#pydantic v2: ConfigDict

