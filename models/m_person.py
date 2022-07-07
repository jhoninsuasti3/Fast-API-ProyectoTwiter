#Libraries Python
from doctest import Example
from typing import Optional
from enum import Enum
from unittest.mock import DEFAULT

# Pydantic
from pydantic import BaseModel, EmailStr, Field, HttpUrl


#Models after this comment

class HairColor(Enum):
    white: str = 'white'
    black: str = 'black'
    brown: str = 'brown'
    red: str = 'red'
    blonde: str = 'blonde'
    tinted: str = 'tinted'

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length= 1,
        max_length= 50,
        example = "Jhon"
    )
    last_name: str = Field(
        ...,
        min_length= 1,
        max_length= 50,
        example = "Insuasti"
    )
    age: int = Field(
        ...,
        gt = 0,
        le = 115,
        example = 30
    )
    hair_color: Optional[HairColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None, example= True)
    email: EmailStr = Field(..., example="aquicorreo@email.com")
    website_url : Optional[HttpUrl] = Field(default=None,example = "https://dashboard.heroku.com/")

    # Class with data for create request automatically
    class Config():
        schema_extra = {
            "example" : {
                 
                        "first_name": "Jhon",
                        "last_name": "Insuasti",
                        "age" : 20,
                        "hair_color": HairColor["blonde"],
                        "is_married": False,
                        "email" : "jhoninsua-03@hotmail.com",
                        "website_url": "https://dashboard.heroku.com/"
            }
        }

class Location(BaseModel):
    
    city : str = Field(
        ...,
        min_length= 2,
        max_length= 30,
    )
    state : str = Field(
        ...,
        min_length= 2,
        max_length= 120,
    )
    country: str = Field(
        ...,
        min_length= 2,
        max_length= 50,
    )

    # Class with data for create request automatically
    class Config():
        schema_extra = {
            "example" : {
                 
                        "city": "Cali",
                        "state": "VValle",
                        "country" : "Colombia"
            }
        }