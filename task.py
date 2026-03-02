class Task:
    def __init__(self, title, book):
        self.title = title
        self.completed = False
        self.book = book
        book.attach_task(self)

    def mark_complete(self):
        self.completed = True
        self.book.mark_completed()

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title} - {status}"