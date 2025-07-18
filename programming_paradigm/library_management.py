class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def return_book(self):
        self.checked_out = False

class Library:
        def __init__(self):
            self._books = []

        def add_book(self, book):
            self._books.append(book)
        
        def check_out_book(self, title):
            for book in self._books:
                if title == book.title:
                    book._is_checked_out = True
        
        def list_available_books(self):
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")

        def return_book(self, title):
            for book in self._books:
                if title == book.title:
                    # book._is_checked_out = False (replacing line with code below)
                    book.return_book()
                    return