class Item:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title


class Book(Item):

    def __init__(self, title, author):
        super().__init__(title)
        self._author = author
        self._status = "available"

    @property
    def author(self):
        return self._author

    @property
    def status(self):
        return self._status

    def borrow(self):
        if self._status == "available":
            self._status = "borrowed"

    def return_book(self):
        if self._status == "borrowed":
            self._status = "available"

    def __str__(self):
        return f"{self.title} by {self.author} - {self.status}"
    
