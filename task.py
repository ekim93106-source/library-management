class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["description"])
        task.completed = data["completed"]
        return task

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"Task: {self.description} - {status}"