class Book:
    TYPES = ('Hardcover', 'Paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, weighting {self.weight}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


# INSTANCE
book = Book('Lei de sullivan', 'Hardcover', 1500)
print(book)

# CLASSMETHOD
book2 = Book.hardcover('Harry Potter', 1500)
book22 = Book.paperback('Overnight', 500)
print(book2)
print(book22)