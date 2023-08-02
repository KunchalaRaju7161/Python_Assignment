import os


class TakeScreenShot:

    @staticmethod
    def takeScreenShot(driver, file_name: str):
        try:
            # Get the current working directory
            current_path = os.getcwd()

            # Create the report path by appending "Reports/" to the current directory path
            reports_path = os.path.join(current_path, "Reports")

            # Ensure the "Reports" directory exists, create it if not present
            if not os.path.exists(reports_path):
                os.makedirs(reports_path)

            # Create the file path for the "index.txt" file located in the "Resources" directory
            index_file_path = os.path.join(current_path, "Resources", "index.txt")

            # Read the content of the "index.txt" file
            with open(index_file_path, 'r') as index_file_in_read:
                data = index_file_in_read.read().strip()

            # Convert the obtained value to an integer and increment it
            current_num = int(data) + 1

            # Convert the incremented value to a string and add an underscore to it
            data = str(current_num) + "_"

            # Write the updated value back to the "index.txt" file
            with open(index_file_path, 'w') as index_file_in_write:
                index_file_in_write.write(data)

            # Take a screenshot using the provided driver and save it to the report path
            driver.save_screenshot(os.path.join(reports_path, data + file_name + ".png"))

            print(f"Screenshot saved at: {reports_path}/{data + file_name}.png")
        except Exception as e:
            # Handle any exceptions that occur during screenshot capture
            print("An error occurred while capturing the screenshot:", e)
