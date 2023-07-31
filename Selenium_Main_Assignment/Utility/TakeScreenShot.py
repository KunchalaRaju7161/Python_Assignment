import os


class TakeScreenShot:

    @staticmethod
    def takeScreenShot(self, driver, file_name: str):
        # Get the current working directory
        current_path = os.getcwd()

        # Find the parent directory containing "Tests" in it's name
        sub_working_path = current_path[0:current_path.find("Tests")]

        # Create the report path by appending "Reports/" to the parent directory path
        reports_path = current_path[0:current_path.find("Tests")] + "Reports/"

        # Create the file path for the "index.text" file located in the "Resources" directory
        index_file_path = current_path[0:current_path.find("Tests")] + "Resources/index.text"

        # Read the content of the "index.txt" file
        index_file_in_read = open(index_file_path, 'r')
        data = index_file_in_read.read()
        data = data.split("_")[0]
        current_num = int(data)

        # Increment the value obtained from the "index.txt" file
        current_num += 1

        # Convert the incremented values to a string and add an underscore to it
        data = str(current_num) + "_"
        index_file_in_read.close()

        # Write the updated values back to the "index.txt" file
        index_file_in_write = open(index_file_path, 'w')
        index_file_in_write.write(data)
        index_file_in_write.close()

        try:
            # Take a screenshot using the provided driver and save it to the report path
            driver.save_screenshort(reports_path + data + file_name + ".png")
        except Exception as e:
            # Handle any exceptions that occur during screenshot capture
            print("File name colud be duplicate/Invalid, for more details read the error message below :\n,", e)
