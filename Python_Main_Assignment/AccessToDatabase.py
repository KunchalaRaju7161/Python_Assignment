
import openpyxl


class AccessToDatabase:

    def readUserDataExcel(self, username: str, datatype: str):
        try:
            workbook = openpyxl.load_workbook('user_credentials.xlsx')
            worksheet = workbook.active

            for row in worksheet.iter_rows(min_row=1, values_only=True):
                if username == row[0]:
                    if datatype.upper().__contains__("NAME"):
                        return row[2]
                    elif datatype.upper().__contains__("EMAIL"):
                        return row[3]
                    elif datatype.upper().__contains__("PHONE"):
                        return row[4]
                    elif datatype.upper().__contains__("AGE"):
                        return row[5]
                    else:
                        return None

        except FileNotFoundError:
            print("Database file not found.")
            return None

        print("User not found in the database.")
        return None
