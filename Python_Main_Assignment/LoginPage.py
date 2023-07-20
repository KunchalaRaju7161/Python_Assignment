# create Loginpage
class LoginPage():

    __userName = "Invalid"
    __password = "Invalid"

    def __init__(self):
        runFlage = True
        while runFlage:
            print("******************** Welcome To User Login Page **************")
            print("--------Please enter yout login credentials------")
            self.__userName = input("Enter user name : ")
            self.__password = input("Enter user password : ")




