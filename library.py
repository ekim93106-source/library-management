class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class BaseLibraryActions:

    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def get_books(self):
        return self._books


class Library(BaseLibraryActions):

    def list_books(self):
        for book in self.get_books():
            print(book.info())

    def find_book(self, title):
        for book in self.get_books():
            if book.title == title:
                return book

        print("Book not found")
        return None

    def borrow_book(self, title):
        book = self.find_book(title)

        if book:
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'")
            else:
                print("Book is already borrowed")

    def return_book(self, title):
        book = self.find_book(title)

        if book:
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'")
            else:
                print("Book was not borrowed")