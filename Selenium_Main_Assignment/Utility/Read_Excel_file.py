import openpyxl

from Configs.ConfigItems import ConfigItems


class Read_Excel_file(ConfigItems):

    def read_excel_data(self, FILE_PATH, SHEET_NAME):
        try:
            # Load the workbook
            workbook = openpyxl.load_workbook(FILE_PATH)

            # Select the sheet by name
            sheet = workbook[SHEET_NAME]

            # Initialize a list to store the data
            data = []

            # Iterate through rows in the sheet
            for row in sheet.iter_rows(values_only=True):
                # Append each row to the data list
                data.append(row)

            return data
        except KeyError:
            print(f"Error: Sheet '{SHEET_NAME}' not found in the workbook.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    data = read_excel_data(ConfigItems.FILE_PATH, ConfigItems.SHEET_NAME)

    if data:
        for row in data:
            print(row)
