#Importando o fastAPI
from fastapi import FastAPI
#Importando o Enum
from enum import Enum

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

#Criando uma classe para enumerar as opções na documentação da api
class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

#usando o decorador para dizer que o metodo get na raiz("/")
#vai retorna essa função
@app.get("/")
#Criando uma função async que vai ser retornada quando acessar a raiz
async def read_all_books():
    return BOOKS

#Usando o método get com parâmetro
@app.get("/books/title_{book_title}")
#O nome que é passado para o método get ({book_title}) precisa ser igual ao passado para a função
async def get_book_title(book_title):
    return {"book_title": book_title}

#Passando um parâmetro do tipo inteiro
@app.get("/books/id_{book_id}")
async def get_book_id(book_id: int):
    return {"Book id: ": book_id}

#Criando a função que vai controlar a opção escolhida
@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "right"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "left"}