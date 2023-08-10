from API_Assignment.Test_Data.Config import ConfigItems
from API_Assignment.POM.Products import api_returns_20_products, unique_ids, read_excel_data, varify_bulk_data


def test_api_returns_20_products():
    api_returns_20_products()


def test_unique_ids():
    unique_ids()


def test_read():
    read_excel_data(ConfigItems.EXCEL_PATH)


def test_excel_data():
    data = read_excel_data(ConfigItems.EXCEL_PATH)
    varify_bulk_data(data)
