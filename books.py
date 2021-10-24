#Importando o fastAPI
from fastapi import FastAPI

#Criando uma variavel do tipo FastAPI
app = FastAPI()

#usando o decorador para dizer que o metodo get na raiz("/")
#vai retorna essa função
@app.get("/")
#Criando uma função async
async def first_api():
    return {"message": "Hello Andrey Cesar"}