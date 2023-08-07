from logging import getLogger


def assert_response_status(response, expected_status):
    log = getLogger()
    log.info("Checking for response status ====== " + str(expected_status))
    assert response.status_code == expected_status


def assert_response_jsonHeader(response):
    header = "application/json; charset=utf-8"
    log = getLogger()
    log.info("Checking for response header ====== " + header)
    assert response.headers['Content-Type'] == header


def assert_string(str1, str2):
    assert str1 == str2