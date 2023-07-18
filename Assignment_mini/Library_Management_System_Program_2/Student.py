class Student:
    # create constractor with name, student ID Attributes
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

    # It returns a string representation of student objects that include its name and id
    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"

    def get_student_id(self):
        return self.student_id

    def borrow_book(self, book):
        if book.is_available():
            book.set_available(False)
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.set_available(True)
            self.borrowed_books.remove(book)
            return True
        else:
            return False