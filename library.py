import argparse

my_books = ["Harry Potter", "1984", "The Hobbit"]

def show_books():
    if len(my_books) == 0:
        print("There are no books right now.")
        return
    
    print("Here are the books:")
    for b in my_books:
        print(b)

def add_new_book(book_name):
    my_books.append(book_name)
    print(book_name, "was added.")

def borrow_one(book_name):
    if book_name not in my_books:
        print("Sorry, that book is not here.")
    else:
        my_books.remove(book_name)
        print("You borrowed", book_name)

def return_one(book_name):
    my_books.append(book_name)
    print("You returned", book_name)

parser = argparse.ArgumentParser()
commands = parser.add_subparsers(dest="action")

commands.add_parser("list")

add_cmd = commands.add_parser("add")
add_cmd.add_argument("book")

borrow_cmd = commands.add_parser("borrow")
borrow_cmd.add_argument("book")

return_cmd = commands.add_parser("return")
return_cmd.add_argument("book")

arguments = parser.parse_args()

if arguments.action == "add":
    add_new_book(arguments.book)
elif arguments.action == "borrow":
    borrow_one(arguments.book)
elif arguments.action == "return":
    return_one(arguments.book)
elif arguments.action == "list":
    show_books()
else:
    print("Please enter a valid command.")