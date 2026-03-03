import json
from book import Book

FILE_NAME = "books.json"

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump([book.to_dict() for book in books], file, indent=4)

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]
    except FileNotFoundError:
        return []