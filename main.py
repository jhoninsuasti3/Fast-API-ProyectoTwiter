from fastapi import FastAPI

app = FastAPI()


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