#Python
from lib2to3.pytree import Base
from optparse import Option
from typing import Optional

# Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Query 
from fastapi import Body

#Import models
from models import m_person as p

app = FastAPI()


#Models
"""


class Person(BaseModel):
    first_name: str 
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


"""


#Fast operation decorator
@app.get("/")
def home():
    return {"Hello" : "World" }

@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}/detail")
def items(num_item):
    return {"num_item":num_item}


#Request and Response Body
@app.post("/person/new")
def add_person(person: p.Person = Body(...)):
    return "Add person is correct post"

# Validaciones: Query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query( min_length=1, max_length=50),
    age: Optional[str] = Query( max_length=3)
):
    if len(age) > 3:
        return "Solo se permite maximo tres valores para el parametro edad"
    else:
        return {name : age}