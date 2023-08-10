

from API_Assignment.POM.User_api import get_user_data, verify_response_notnull, verify_password


def test_specific_users_presence():
    get_user_data()


def test_verify_response_notnull():
    verify_response_notnull()


def test_verify_password():
    pass_or_fail_bool = verify_password()
    assert pass_or_fail_bool, "invalid password"

