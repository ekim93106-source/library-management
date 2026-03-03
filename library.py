import argparse
from book import Book
from task import Task
from db import load_books, save_books

books = load_books()

def list_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book)

def add_book(name):
    book = Book(name)
    books.append(book)
    save_books(books)
    print("Book added.")

def borrow_book(name):
    for book in books:
        if book.title == name:
            book.borrow()
            save_books(books)
            print("Book borrowed.")
            return
    print("Book not found.")

def return_book(name):
    for book in books:
        if book.title == name:
            book.return_book()
            save_books(books)
            print("Book returned.")
            return
    print("Book not found.")

def add_task(name, task_title):
    for book in books:
        if book.title == name:
            Task(task_title, book)
            print("Reading task added.")
            return
    print("Book not found.")

def complete_task(name):
    for book in books:
        if book.title == name and book._reading_task:
            book._reading_task.mark_complete()
            save_books(books)
            print("Reading completed.")
            return
    print("Task not found.")

def run():
    parser = argparse.ArgumentParser(description="Library Management System")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("name")

    borrow_parser = subparsers.add_parser("borrow")
    borrow_parser.add_argument("name")

    return_parser = subparsers.add_parser("return")
    return_parser.add_argument("name")

    subparsers.add_parser("list")

    task_parser = subparsers.add_parser("addtask")
    task_parser.add_argument("name")
    task_parser.add_argument("task")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("name")

    args = parser.parse_args()

    if args.command == "add":
        add_book(args.name)
    elif args.command == "borrow":
        borrow_book(args.name)
    elif args.command == "return":
        return_book(args.name)
    elif args.command == "list":
        list_books()
    elif args.command == "addtask":
        add_task(args.name, args.task)
    elif args.command == "complete":
        complete_task(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    run()