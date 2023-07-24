import openpyxl


class Update_emp_data():
    def __init__(self):
        self.file_path = 'employee_data.xlsx'
        self.wb = openpyxl.load_workbook(self.file_path)
        self.ws = self.wb.active

    def update_employee_data(self, employee_data, user_id):
        # Check if the User-ID exists in the employee_data dictionary
        if user_id in employee_data:
            record = employee_data[user_id]

            # Ask the user for the field to be updated
            field_to_update = input("Please enter the field to be updated: ")

            # Make sure the field is not "Employee Id" or "User-ID"
            if field_to_update in ["Employee Id", "User-ID"]:
                print("Employee Id and User-ID cannot be updated.")
                return

            # Check if the field exists in the record
            if field_to_update not in record:
                print(f"{field_to_update} field not found in the record.")
                return

            # Ask the user for the updated value
            updated_value = input(f"Please enter the updated value for {field_to_update}: ")

            # Update the field in the employee_data dictionary
            record[field_to_update] = updated_value

            # Display the updated user details
            print("UPDATE SUCCESSFUL AND UPDATED user details are:")
            for key, value in record.items():
                print(f"{key}: {value}")

            # Save the updated workbook
            self.wb.save(self.file_path)

        else:
            print("User-ID not found in the employee_data.")


if __name__ == "__main__":
    emp_data = {
        "Hr-1": {
            "Employee Id": "Em-1",
            "Name": "John",
            "Age": 34,
            "Company-Name": "Sony",
            "Designation": "SDET",
            "Salary": 50000,
            "Address": "ABC Street 713457",
            "Phone Number": 9008765682
        }
    }

    user_id = input("Please enter the User-ID of the record you want to update: ")
    emp_updater = Update_emp_data()
    emp_updater.update_employee_data(emp_data, user_id)
