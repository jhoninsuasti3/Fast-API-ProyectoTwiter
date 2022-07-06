#Python
from lib2to3.pytree import Base
from typing import Optional

# Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI 
from fastapi import Body

app = FastAPI()


#Models

class Person(BaseModel):
    first_name: str 
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

#Fast operation decorator
@app.get("/")
def home():
    return {"Hello" : "World" }

@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}/detail?ubicacion=CaliColombia&nombre_usuario=jaim4839")
def items(num_item):
    return {"num_item":num_item}


#Request and Response Body
@app.post("/person/new")
def add_person(person: Person = Body(...)):
    return "Add person is correct post"