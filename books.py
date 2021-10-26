#Importando o fastAPI
from fastapi import FastAPI

#Criando uma variavel do tipo FastAPI
app = FastAPI()

#Dicionario com o nome 'BOOKS'
BOOKS ={
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

#usando o decorador para dizer que o metodo get na raiz("/")
#vai retorna essa função
@app.get("/")
#Criando uma função async que vai ser retornada quando acessar a raiz
async def first_api():
    return {"message": "Hello Andrey Cesar"}