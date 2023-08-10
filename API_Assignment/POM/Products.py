import unittest

import jsonschema
import pandas as pd
import openpyxl
import requests
from _pytest.outcomes import fail

from API_Assignment.Test_Data.Config import ConfigItems
from API_Assignment.Utility.CommonAssersions import assert_response_status, assertEqualWithMessage

base_url = ConfigItems.API_URL


def api_returns_20_products():
    response = requests.get(base_url)
    assert_response_status(response, 200)
    products = response.json()
    assert len(products) == 20, "API did not return 20 products"


def unique_ids():
    response = requests.get(base_url)
    assert_response_status(response, 200)
    products = response.json()
    ids = [product["id"] for product in products]
    assertEqualWithMessage(len(ids), len(set(ids)), "Not all IDs are unique")


def read_excel_data(excel_file):
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


def varify_bulk_data(data:list):
    for each_payload in data:
        # Sending the POST request
        response = requests.post(base_url, data=each_payload)
        # Checking the response
        if response.status_code == 200:
            print('POST request successful!')
            print('Response:', response.text)
        else:
            print('POST request failed. Status code:', response.status_code)







