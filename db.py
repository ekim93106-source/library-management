import json

FILE_NAME = "books.json"

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)