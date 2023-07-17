from datetime import datetime, timedelta

from Assignment_mini.Program_2.Book import Book
from Assignment_mini.Program_2.Student import Student


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_all_books(self):
        for book in self.books:
            print(book)

    def display_available_books(self):
        for book in self.books:
            if book.is_available():
                print(book)

    def display_overdue_books(self):
        today = datetime.now()
        for book in self.books:
            if not book.is_available() and today > book2.due_date:
                print(book)

    def borrow_book(self, student, book):
        return student.borrow_book(book)

    def return_book(self, student, book):
        return student.return_book(book)


# Testing the implementation
if __name__ == "__main__":
    # Creating book instances
    book1 = Book("Hind Swaraj", "Mahatma Gandhi","9781850656814")
    book2 = Book("discovery of india", "Jawaharlal Nehru","0-670-05801-7")
    book3 = Book("wings of fire", "A P J Abdul Kalam","81-7371-146-1")

    # Creating student instances
    student1 = Student("Kunchala Raju", "S001")
    student2 = Student("Nithish", "S002")

    print(student1)

    # Creating library instance
    library = Library()

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Displaying all books in the library
    print("All books in the library:")
    library.display_all_books()
    print()

    # Displaying available books
    print("Available books:")
    library.display_available_books()
    print()

    # Student1 borrows book1
    print("Student1 borrows book1:", library.borrow_book(student1, book1))
    print()

    # Displaying borrowed books by Student1
    print("Books borrowed by Student1:")
    for book in student1.borrowed_books:
        print(book)
    print()

    # Student1 returns book1
    print("Student1 returns book1:", library.return_book(student1, book1))
    print()

    # Displaying available books
    print("Available books:")
    library.display_available_books()
    print()

    # Student2 tries to borrow book1 (already borrowed by Student1)
    print("Student2 tries to borrow book1:", library.borrow_book(student2, book1))
    print()

    # Displaying overdue books (assuming due_date is 7 days from today)
    book2.due_date = datetime.now() - timedelta(days=7)
    print("Overdue books:")
    library.display_overdue_books()
