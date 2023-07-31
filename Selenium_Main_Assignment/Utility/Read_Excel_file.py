import openpyxl

from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems


class Read_Excel_file(ConfigItems):

    def read_excel_data(self,file_path, sheet_name):
        try:
            # Load the workbook
            workbook = openpyxl.load_workbook(file_path)

            # Select the sheet by name
            sheet = workbook[sheet_name]

            # Initialize a list to store the data
            data = []

            # Iterate through rows in the sheet
            for row in sheet.iter_rows(values_only=True):
                # Append each row to the data list
                data.append(row)

            return data
        except KeyError:
            print(f"Error: Sheet '{sheet_name}' not found in the workbook.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    data = read_excel_data(ConfigItems.file_path,ConfigItems.sheet_name)

    if data:
        for row in data:
            print(row)
