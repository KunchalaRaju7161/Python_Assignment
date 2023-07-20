# create RegisterNewUser class
class RegisterNewUser():
    # Employee records dictionary to store employee details
    employee_records = {}

    def register_screen(self):
        print("******************** Welcome To User Registration Page **************")
        print("------------------- New User Registration Form -------------")
        RegisterNewUser().new_user_register()

    def new_user_register(self):
        while True:
            print("Employee Registration")
            self.user_id = input("Enter user-id : ")
            # check if user-id already exists
            if self.user_id in self.employee_records:
                print("user -id already exists. Please use a different User -id")
                return
            user_name = input("Enter user name : ")
            password = input("Enter user password : ")
            if not self.validate_password(password):
                print("Invalid Password!")
                print("password should be in the range of 5 to 10 characters")
                print("at lest one uppercase, one lowercase, one digit, and one special character")
                return
            confirm_password = input("Enter user confirm password : ")

            if password == confirm_password:
                print("Registration successful")
                break
            else:
                print("Registration unsuccessful")
                print("Your provided wrong details")

    def validate_age(self, age):
        return 18 <= age <= 90

    def validate_salary(self, salary):
        return salary > 0

    def validate_phone_number(self, phone_number):
        # check if the phone number contains exactly 10 digits
        if len(phone_number) != 10:
            return False
        # check if all characters in phone number are digits
        if not phone_number.isdigit():
            return False

        return True

    def validate_password(self, password):
        # password should be in the range of 5 to 10 characters
        if 5 <= len(password) <= 10:
            # check for at lest one uppercase, one lowercase, one digit, and one special character
            if any(char.isupper() for char in password) and \
                    any(char.islower() for char in password) and \
                    any(char.isdigit() for char in password) and \
                    any(char in "@#$&*!" for char in password):
                return True
        return False

