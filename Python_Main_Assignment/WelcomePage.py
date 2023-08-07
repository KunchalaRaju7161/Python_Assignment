# create WelcomePage class
from Python_Main_Assignment.LoginPage import LoginScreen
from Python_Main_Assignment.RegisterNewUser import RegisterNewUser


class WelcomePage:
    # create a constractor
    def __init__(self):
        while True:
            print("************************** Welcome To User Database ********************")
            print("1. Login")
            print("2. Registration")
            print("3. Exit")
            print("-------------------------------------------------------")
            option = input("Please enter option 1,2 or 3 to proceed : ")
            print("\n")
            self.user_selection(option)

    def user_selection(self, option):
        try:
            if option == "1":
                LoginScreen().run_login()
            elif option == "2":
                RegisterNewUser().register_screen()
            elif option =="3":
                exit()
            else:
                print(" Warning : You have entered the invalid option")
                print("please select valid option")
                WelcomePage()
        except Exception as e:
            print("Sorry! Error occured in the application", e)


WelcomePage()


