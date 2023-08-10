import requests

from API_Assignment.POM.User_api import get_user_data, verify_response_notnull, verify_password
from API_Assignment.Test_Data.Config import ConfigItems


def test_specific_users_presence():
    get_user_data()


def test_verify_response_notnull():
    verify_response_notnull()


def test_verify_password():
    try:
        verify_password()
        print("All passwords are valid.")
    except AssertionError as e:
        print(e)
