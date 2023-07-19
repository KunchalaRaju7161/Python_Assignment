# create welcome class
class Welcome_Page:
    def __init__(self):
        while True:
            print("****************** Welcome to User Database **********************")
            print("1. Login ")
            print("2. Registration ")
            print("3. Exit ")
            print("\n")
            self.userSelection()

    def userSelection(self):
        option = input("Please enter 1 or 2 or 3 to proceed : ")

        # if option == '1':


Welcome_Page()