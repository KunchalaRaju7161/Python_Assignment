# create WelcomePage class
import openpyxl

from Python_Main_Assignment.Update_emp_data import Update_emp_data
from Python_Main_Assignment.Userdata import Userdata


class UserLoginScreen():
    # create a constractor
    def __init__(self):
        while True:
            print("************************** Welcome to User Database ********************")
            print("1. Add User Data ")
            print("2. List User Data ")
            print("3. Update User Data ")
            print("4. Delete User Data  ")
            print("5. Exit ")
            print("-------------------------------------------------------")
            option = input("Please enter option 1,2,3,4 or 5 to proceed : ")
            print("\n")
            self.user_selection(option)

    def user_selection(self, option):
        try:
            if option == "1":
                Userdata().added_User_Data()
            elif option == "2":
                Userdata().display_employee_data1()
            elif option == "3":
                Update_emp_data().update_employee_data(employee_data={
                    "User-ID" : "Hr-1",
                    "Employee Id":"Em-1",
                    "Name": "John",
                    "Age": 34,
                    "Company-Name": "Sony",
                    "Designation": "SDET",
                    "Salary": 50000,
                    "Address": "ABC Street 713457",
                    "Phone Number": 9008765682
                }, user_id="Hr-1")
            elif option == "4":
                print("hi")
                # Userdata().delete_rows_by_value("Sheet1",2, "ValueToDelete")
            elif option == "5":
                exit()

            else:
                print(" Warning : You have entered the invalid option")
                print("please select valid option")
                UserLoginScreen()
        except Exception as e:
            print("Sorry! Error occured in the application", e)
