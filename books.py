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
async def read_all_books():
    return BOOKS

#Usando o método get com parâmetro
@app.get("/books/{book_title}")
#O nome que é passado para o método get ({book_title}) precisa ser igual ao passado para a função
async def get_book_title(book_title):
    return {"book_title": book_title}