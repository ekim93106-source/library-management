import argparse

books = ["Harry Potter", "1984", "The Hobbit"]

def list_books():
    if books:
        print("Books:")
        for book in books:
            print("-", book)
    else:
        print("No books available.")

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

parser = argparse.ArgumentParser(description="Library System")
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("list")
add = subparsers.add_parser("add")
add.add_argument("name")

borrow = subparsers.add_parser("borrow")
borrow.add_argument("name")

ret = subparsers.add_parser("return")
ret.add_argument("name")

args = parser.parse_args()

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