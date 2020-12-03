class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


# shelf = BookShelf(300)

class Book:
    def __init__(self, name):
        self.name = name

book1 = Book('Harry Potter')
book2 = Book('Lord of Rings')
book3 = Book('Nárnia')
shelf = BookShelf(book1, book2, book3)
print(shelf)