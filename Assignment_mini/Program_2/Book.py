class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_isbn(self):
        return self.isbn

    def is_available(self):
        return self.available

    def set_available(self, status):
        self.available = status

