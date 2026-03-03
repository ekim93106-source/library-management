import argparse
from library import Library

def main():
    library = Library()

    parser = argparse.ArgumentParser(description="Library Management System")

    subparsers = parser.add_subparsers(dest="command")

    # Add Book
    add_parser = subparsers.add_parser("add", help="Add a new book")
    add_parser.add_argument("title", help="Title of the book")
    add_parser.add_argument("author", help="Author of the book")

    # Borrow Book
    borrow_parser = subparsers.add_parser("borrow", help="Borrow a book")
    borrow_parser.add_argument("title", help="Title of the book")

    # Return Book
    return_parser = subparsers.add_parser("return", help="Return a book")
    return_parser.add_argument("title", help="Title of the book")

    # List Books
    subparsers.add_parser("list", help="List all books")

    # Add Task
    add_task_parser = subparsers.add_parser("addtask", help="Add a task")
    add_task_parser.add_argument("title", help="Task title")

    # Complete Task
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("title", help="Task title")

    args = parser.parse_args()

    if args.command == "add":
        library.add_book(args.title, args.author)

    elif args.command == "borrow":
        library.borrow_book(args.title)

    elif args.command == "return":
        library.return_book(args.title)

    elif args.command == "list":
        library.list_books()

    elif args.command == "addtask":
        library.add_task(args.title)

    elif args.command == "complete":
        library.complete_task(args.title)

    else:
        parser.print_help()


if __name__ == "__main__":
    print("Library system starting...")
    main()