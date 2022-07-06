#Libraries Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field


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
        max_length= 50
    )
    last_name: str = Field(
        ...,
        min_length= 1,
        max_length= 50
    )
    age: int = Field(
        ...,
        gt = 0,
        le = 115
    )
    hair_color: Optional[HairColor] = Field(default=None )
    is_married: Optional[bool] = Field(default=None)

class Location(BaseModel):
    city : str
    state : str
    country: str