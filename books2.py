from fastapi import FastAPI
#Model para classes
from pydantic import BaseModel, Field
#Para gerar id unicas
from uuid import UUID
#Para criar campos opcionais
from typing import Optional

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

BOOKS = []

@app.get("/")
async def read_all_books():
    if leb(BOOKS) <1:
        create_book_no_api()
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

def create_book_no_api():
    book_1 = Book(id="00b2d180-4f22-4e9f-bdf1-7566ad22b366", title="Titulo 1", author="Autor 1", description="Descrição 1", rating=50)
    BOOKS.append(book_1)