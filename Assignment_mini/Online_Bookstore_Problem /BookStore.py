import openpyxl

path = "/Users/rkunchala/pythonAssignments/Python_Assignments/Assignment_mini/Resource/OnlineBookstore.xlsx"

obj = openpyxl.load_workbook(path)
sheet_obj = obj.active
max_col = sheet_obj.max_column

books = []
for i in range(2, max_col + 1):
    cell_obj = sheet_obj.cell(row=1, column=i)
    books.append(cell_obj.value)

prices = []
for i in range(2, max_col + 1):
    cell_obj = sheet_obj.cell(row=2, column=i)
    prices.append(cell_obj.value)

threshold = 50


def filter_books(books, prices, threshold):
    filtered_books = []
    for book, price in zip(books, prices):
        if price > threshold:
            filtered_books.append(book)
    return filtered_books


def calculate_total_revenue(prices, threshold):
    total_revenue = sum(price for price in prices if price > threshold)
    return total_revenue


filter_book = filter_books(books, prices, threshold)
revenue = calculate_total_revenue(prices, threshold)

book_price_tuple = list(zip(books, prices))

print("Filtered books : ", filter_book)
print("Total revenue : ", revenue)
print("Book prices tuples : ", book_price_tuple)
