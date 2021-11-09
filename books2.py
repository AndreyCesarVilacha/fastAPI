from fastapi import FastAPI, HTTPException, Request, status, Form, Header
#Model para classes
from pydantic import BaseModel, Field
#Para gerar id unicas
from uuid import UUID
#Para criar campos opcionais
from typing import Optional
from starlette.responses import JSONResponse

class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Descrição do livro", max_length=100,min_length=1)
    rating: int = Field(gt=-1, lt=101)

    #muda o schema do docs para este exemplo
    class Config:
        schema_extra = {
            "example":{
                "id":"2b3d070-4f22-4e9f-bdf1-7566ad22b366",
                "title": "Ciência da Computânção para Pros com python",
                "author": "Andrey Cesar",
                "description": "Uma descrição completa e bonita para o exemplo",
                "rating": 75
            }
        }

class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(
        None, 
        title="description of the Book", 
        max_length=100, 
        min_length=1
    )

BOOKS = []

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request,
                                            exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Hey, why do you want {exception.books_to_return}"
                            f"books? You need to read more!"}
    )

@app.post("/books/login")
async def book_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.get("/header")
async def read_header(random_header: Optional[str] = Header(None)):
    return {"Random-Header": random_header}

@app.get("/", status_code=status.HTTP_201_CREATED)
async def read_all_books(books_to_return: Optional[int]= None):

    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)

    if len(BOOKS) <1:
        create_book_no_api()

    #Retorna um livro especifico de BOOKS, ou retorna todos caso não encontre na query
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i=1
        new_books = []

        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i +=1
        return new_books
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id ==book_id:
            return x
    raise raise_item_cannot_be_found_exception()

#Converte os dados para a Classe BookNoRating
@app.get("/book/rating/{book_id}", response_model=BookNoRating)
async def read_book_no_rating(book_id:UUID):
    for x in BOOKS:
        if x.id ==book_id:
            return x
    raise raise_item_cannot_be_found_exception()

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_cannot_be_found_exception()

@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKs:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'D: {book_id} deleted'
    raise raise_item_cannot_be_found_exception()

def create_book_no_api():
    book_1 = Book(id="00b2d180-4f22-4e9f-bdf1-7566ad22b366", title="Titulo 1", author="Autor 1", description="Descrição 1", rating=50)
    BOOKS.append(book_1)

def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,
                         detail="Book not found",
                         headers={"X=Header_Error":
                                  "Nothing to be seen at the UUID"})