class Book:
    TYPES = ('Hardcover', 'Paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"Book {self.name}, {self.book_type}, weighting {self.weight}"

    @classmethod
    def hardcover(cls, name: str, page_weight: float) -> 'Book':
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: float) -> 'Book':
        return cls(name, cls.TYPES[1], page_weight)


# INSTANCE
book = Book('Lei de sullivan', 'Hardcover', 1500)
print(book)

# CLASSMETHOD
book2 = Book.hardcover('Harry Potter', 1500)
book22 = Book.paperback('Overnight', 500)
print(book2)
print(book22)