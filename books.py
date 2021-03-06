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

#Função que retorna um valor do dicionario BOOKS
@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

#Criando uma função query para eliminar o book_3 do dicionario
@app.get("/books/filter")
async def filter_book_3(skip_book: str = 'book_3'):
    new_books = BOOKS.copy()
    del new_books[skip_book]
    return new_books

#Adicionando um valor ao dicionario
@app.post("/books/post")
#Os valores que devem para criar uma nova entrada no dicionario
async def create_book(book_title, book_author):
    #Var para indicar qual é o id atual
    current_book_id = 0

    #Confere se já existe uma entrada no dicionário
    if len(BOOKS) > 0:
        #Percorre os elementos no dicionario
        for book in BOOKS:
            #Passa o valor do tamnaho do dicionario para a val x
            x = int(book.split('_')[-1])
            #Verifica se a val x é maior que o id atual
            if x > current_book_id:
                #atribui o valor de x para o id atual
                current_book_id = x
    #Cria a entrada no dicionario passando os valores para a entrada
    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    #Retorna o novo dicionario com a nova entrada
    return BOOKS[f'book_{current_book_id + 1}']

@app.put("/books/{book_name}")
#Passando para a função as informações que queremos mudar
async def update_book(book_name: str, book_title: str, book_author: str):
    #uma val para armazenar o novo titulo e o novo autor
    book_information = {'title': book_title, 'author': book_author}
    #Passamos esse novo valor para o local escolhido
    BOOKS[book_name] = book_information
    #Retornamos a val com os novos valores
    return book_information

@app.delete("/books/{book_name}")
#Criando uma função que deleta a entrada
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted.'