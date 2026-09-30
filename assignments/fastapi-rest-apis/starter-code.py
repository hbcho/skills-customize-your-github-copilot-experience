from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Library Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookCreate(BaseModel):
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
}


# TODO: Add GET /books to return all books.
# TODO: Add GET /books/{book_id} to return one book or a 404 response.
# TODO: Add POST /books to create a book using BookCreate.
# TODO: Add PUT /books/{book_id} to update an existing book.
# TODO: Add DELETE /books/{book_id} to remove a book.