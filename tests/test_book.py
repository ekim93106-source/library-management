from book import Book

def test_book_creation():
    b = Book("Test Title", "Test Author")
    assert b.title == "Test Title"
    assert b.author == "Test Author"