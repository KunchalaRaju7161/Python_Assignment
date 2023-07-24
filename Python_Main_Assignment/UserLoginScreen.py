# create WelcomePage class


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

                # LoginScreen().run_login()
                print("hi")
            elif option == "2":
                print("hi1")
            elif option == "3":
                exit()
            else:
                print(" Warning : You have entered the invalid option")
                print("please select valid option")
                UserLoginScreen()
        except Exception as e:
            print("Sorry! Error occured in the application", e)
