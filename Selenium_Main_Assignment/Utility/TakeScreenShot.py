import os


class TakeScreenShot:

    @staticmethod
    def takeScreenShot(driver, file_name: str):
        current_path = os.getcwd()
        sub_working_path = current_path[0:current_path.find("Tests")]
        reports_path = current_path[0:current_path.find("Tests")] + "Reports/"
        index_file_path = current_path[0:current_path.find("Tests")] + "Resources/index.txt"

        index_file_in_read = open(index_file_path, 'r')
        data = index_file_in_read.read()
        data = data.split("_")[0]
        current_num = int(data)
        current_num += 1
        data = str(current_num) + "_"
        index_file_in_read.close()

        index_file_in_write = open(index_file_path, 'w')
        index_file_in_write.write(data)
        index_file_in_write.close()

        try:
            driver.save_screenshot(reports_path + data + file_name + ".png")
        except Exception as e:
            print("File name could be duplicate/Invalid, for more details read error the below error mesaage:\n,", e)
