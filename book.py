class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")