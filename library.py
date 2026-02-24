import argparse

# Simple book storage
books = ["Harry Potter", "1984", "The Hobbit"]


# Functions
def list_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Available books:")
        for book in books:
            print("- " + book)


def add_book(name):
    books.append(name)
    print("Book added.")


def borrow_book(name):
    if name in books:
        books.remove(name)
        print("Book borrowed.")
    else:
        print("Book not available.")


def return_book(name):
    books.append(name)
    print("Book returned.")


# CLI Setup
parser = argparse.ArgumentParser(description="Simple Library Management System")

subparsers = parser.add_subparsers(dest="command")

# add command
add_parser = subparsers.add_parser("add")
add_parser.add_argument("name")

# borrow command
borrow_parser = subparsers.add_parser("borrow")
borrow_parser.add_argument("name")

# return command
return_parser = subparsers.add_parser("return")
return_parser.add_argument("name")

# list command
subparsers.add_parser("list")

args = parser.parse_args()

# Connect commands to functions
if args.command == "add":
    add_book(args.name)

elif args.command == "borrow":
    borrow_book(args.name)

elif args.command == "return":
    return_book(args.name)

elif args.command == "list":
    list_books()

else:
    parser.print_help()