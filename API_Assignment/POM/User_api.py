import json
import re
import requests
from API_Assignment.Test_Data.Config import ConfigItems
from API_Assignment.Utility.LogDetails import LogDetails

url = ConfigItems.USER_API_URL
logging = LogDetails.getLogger(ConfigItems.LOGGER_PATH)


def get_user_data():
    logging.info("Fetching user data from the API...")
    response = requests.get(url)
    response_str_data = str(response.json())
    data = ['david', 'don', 'miriam']
    for each_value in data:
        match_info = re.findall(each_value.lower(), response_str_data.lower())
        if match_info:
            logging.info("Match found and passed for : %s", each_value)

        else:
            logging.error("Match not found : %s", each_value)
            logging.debug("API Response: %s", response.json())
            assert False, "Match not found"


def verify_response_notnull():
    logging.info("Fetching user data from the API...")
    response = requests.get(url)
    logging.info("API response received successfully.")
    response_json = response.json()
    json_final_response = json.dumps(response_json, indent=4)
    dict_response = json.loads(json_final_response)
    for each_address_index in range(0, len(dict_response)):
        assert dict_response[each_address_index]['address']['geolocation'][
                   'lat'] != None, "latitud value for address " + str(each_address_index + 1) + " has None Value"
        assert dict_response[each_address_index]['address']['geolocation'][
                   'long'] != None, "long value for address " + str(each_address_index + 1) + " has None Value"


def is_valid_password(password):
    # Check for at least 1 character
    if not any(c.isalpha() for c in password):
        return False

    # Check for at least 1 special character
    if not any(c for c in password if c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"):
        return False

    # Check for at least 1 number
    if not any(c.isdigit() for c in password):
        return False

    return True


def verify_password():
    logging.info("Fetching user data from the API...")
    response = requests.get(url)
    logging.info("API response received successfully.")
    response_json = response.json()
    json_final_response = json.dumps(response_json, indent=4)
    dict_response = json.loads(json_final_response)
    for each_address_index in range(0, len(dict_response)):
        passwords = dict_response[each_address_index]['password']
        logging.info("Verifying password format for: %s", passwords)
        if is_valid_password(passwords) == False:
            logging.error("Invalid Format Password : %s", passwords)
            return False

    return True
