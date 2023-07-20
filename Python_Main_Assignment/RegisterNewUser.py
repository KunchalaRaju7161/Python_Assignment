# create RegisterNewUser class
class RegisterNewUser():

    def register_screen(self):
        print("******************** Welcome To User Registration Page **************")
        print("------------------- New User Registration Form -------------")
        RegisterNewUser().new_user_register()

    def new_user_register(self):
        while True:
            user_name = input("Enter user name : ")
            password = input("Enter user password : ")
            confirm_password = input("Enter user confirm password : ")

            if password == confirm_password:
                print("Registration successful")
                break
            else:
                print("Registration unsuccessful")
                print("Your provided wrong details")


