from fastapi import FastAPI
#Model para classes
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Descrição do livro", max_length=100,min_length=1)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []

@app.get("/")
async def read_all_books():
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book