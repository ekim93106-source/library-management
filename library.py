import argparse
from db import load_books, save_books

books = load_books()

def list_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book)

def add_book(title, author):
    from book import Book
    book = Book(title, author)
    books.append(book)
    save_books(books)
    print("Book added.")

def borrow_book(title):
    for book in books:
        if book.title == title:
            book.borrow()
            save_books(books)
            return
    print("Book not found.")

def return_book(title):
    for book in books:
        if book.title == title:
            book.return_book()
            save_books(books)
            return
    print("Book not found.")

def add_task(title, task_description):
    for book in books:
        if book.title == title:
            book.add_task(task_description)
            save_books(books)
            return
    print("Book not found.")

def complete_task(title):
    for book in books:
        if book.title == title:
            book.complete_task()
            save_books(books)
            return
    print("Book not found.")

def run():
    parser = argparse.ArgumentParser(description="Library Management System")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("author")

    borrow_parser = subparsers.add_parser("borrow")
    borrow_parser.add_argument("title")

    return_parser = subparsers.add_parser("return")
    return_parser.add_argument("title")

    subparsers.add_parser("list")

    task_parser = subparsers.add_parser("addtask")
    task_parser.add_argument("title")
    task_parser.add_argument("task")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("title")

    args = parser.parse_args()

    if args.command == "add":
        add_book(args.title, args.author)
    elif args.command == "borrow":
        borrow_book(args.title)
    elif args.command == "return":
        return_book(args.title)
    elif args.command == "list":
        list_books()
    elif args.command == "addtask":
        add_task(args.title, args.task)
    elif args.command == "complete":
        complete_task(args.title)
    else:
        parser.print_help()