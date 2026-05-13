from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin"),
    Book(id=2, title="Fluent Python", author="Luciano Ramalho"),
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    if any(existing.id == book.id for existing in books):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return {"message": "Book created", "book": book}


# TODO: Implement PUT /books/{book_id}
# TODO: Implement DELETE /books/{book_id}
