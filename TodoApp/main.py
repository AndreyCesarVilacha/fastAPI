from fastapi import FastAPI
#Importandos os modelos criados
import models
#Importando a engine de database que criamos
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def create_database():
    return {"Database": "Created"}