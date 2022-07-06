#Libraries
from typing import Optional

# Pydantic
from pydantic import BaseModel


#Models after this comment

class Person(BaseModel):
    first_name: str 
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None