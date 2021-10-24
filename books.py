#Importando o fastAPI
from fastapi import FastAPI

#Criando uma variavel do tipo FastAPI
app = FastAPI()

#usando o decorador para dizer que o metodo get na raiz("/")
#vai retorna essa função
@app.get("/")
#Criando uma função async que vai ser retornada quando acessar a raiz
async def first_api():
    return {"message": "Hello Andrey Cesar"}