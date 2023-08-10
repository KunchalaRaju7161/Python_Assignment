import openpyxl
import requests
from API_Assignment.Test_Data.Config import ConfigItems
from API_Assignment.Utility.CommonAssersions import assert_response_status, assertEqualWithMessage
from API_Assignment.Utility.LogDetails import LogDetails

base_url = ConfigItems.API_URL
logging = LogDetails.getLogger(ConfigItems.LOGGER_PATH)


def api_returns_20_products():
    logging.info("Fetching data from the API...")
    response = requests.get(base_url)
    assert_response_status(response, 200)
    logging.info("API response received successfully.")
    products = response.json()
    assert len(products) == 20, "API did not return 20 products"
    logging.info("API returned 20 products as expected.")


def unique_ids():
    logging.info("Fetching data from the API...")
    response = requests.get(base_url)
    assert_response_status(response, 200)
    logging.info("API response received successfully.")
    products = response.json()
    ids = [product["id"] for product in products]
    assertEqualWithMessage(len(ids), len(set(ids)), "Not all IDs are unique")
    logging.info("All IDs in the API response are unique.")


def read_excel_data(excel_file):
    logging.info("Reading data from Excel file: %s", excel_file)
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook['Sheet1']
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        product = {
            "title": row[0],
            "price": row[1],
            "description": row[2],
            "image": row[3],
            "category": row[4]
        }
        data.append(product)

    return data


def varify_bulk_data(data: list):
    for each_payload in data:
        # Sending the POST request
        response = requests.post(base_url, data=each_payload)
        # Checking the response
        if response.status_code == 200:
            logging.info('POST request successful!')
            logging.info('Response: %s', response.text)
        else:
            print('POST request failed. Status code:', response.status_code)
            logging.error('POST request failed. Status code: %d', response.status_code)

