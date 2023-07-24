import openpyxl

from Python_Main_Assignment.UserLoginScreen import UserLoginScreen


class LoginScreen:
    def __init__(self):
        self.run_login()

    def read_credentials_from_excel(self, filename):
        credentials = []
        try:
            workbook = openpyxl.load_workbook(filename)
            sheet = workbook.active

            for row in sheet.iter_rows(values_only=True):
                username, password = row
                credentials.append((username, password))

            workbook.close()
        except Exception as e:
            print("Error reading credentials from Excel:", e)

        # print("Credentials from Excel:", credentials)  # Add this line to check the read data
        return credentials

    def check_login(self, username, password, credentials):
        for registered_username, registered_password in credentials:
            if username == registered_username and password == registered_password:
                return True
        return False

    def run_login(self):
        filename = "user_credentials.xlsx"
        registered_credentials = self.read_credentials_from_excel(filename)

        print("Welcome to the Login Portal!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # print("User Input: Username={}, Password={}".format(username, password))  # Add this line to check user input

        if self.check_login(username, password, registered_credentials):
            print("Login successful! Welcome to login, {}".format(username))
            UserLoginScreen()
        else:
            print("Invalid login credentials. Please try again.")



