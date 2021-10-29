from fastapi import FastAPI
#Model para classes
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int

BOOKS = []

@app.get("/")
async def read_all_books():
    return BOOKS