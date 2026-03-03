from task import Task

class Book:
    def __init__(self, title, author, available=True, task=None):
        self.title = title
        self.author = author
        self.available = available
        self.reading_task = task  # relationship

    def borrow(self):
        if self.available:
            self.available = False
            print("You borrowed the book.")
        else:
            print("Book already borrowed.")

    def return_book(self):
        self.available = True
        print("You returned the book.")

    def add_task(self, description):
        self.reading_task = Task(description)
        print("Reading task added.")

    def complete_task(self):
        if self.reading_task:
            self.reading_task.mark_complete()
            print("Reading completed.")
        else:
            print("No task found.")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available,
            "reading_task": self.reading_task.to_dict() if self.reading_task else None
        }

    @staticmethod
    def from_dict(data):
        task = Task.from_dict(data["reading_task"]) if data.get("reading_task") else None
        return Book(
            data["title"],
            data["author"],
            data.get("available", True),
            task
        )

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        task_info = f" | {self.reading_task}" if self.reading_task else ""
        return f"{self.title} by {self.author} - {status}{task_info}"