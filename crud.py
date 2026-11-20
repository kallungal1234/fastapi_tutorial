from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publish_date": "1988-01-01"
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publish_date": "2018-10-16"
    },
    {
        "id": 3,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "publish_date": "1997-04-01"
    },
    {
        "id": 4,
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "publish_date": "2020-09-08"
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str
    
    
@app.post("/add-book")
def add_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)

    return {
        "message": "Book added successfully",
        "book": new_book
    }
    
class BookUpdate(BaseModel):
    title: str
    author: str
    publish_date: str

@app.put("/update-book/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publish_date'] = book_update.publish_date
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
@app.delete("/delete-book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return (f"Book removed. book id: {book_id}")  
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
