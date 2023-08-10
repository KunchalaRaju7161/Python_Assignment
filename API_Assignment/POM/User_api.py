import json
import re

import requests

from API_Assignment.Test_Data.Config import ConfigItems

url = ConfigItems.USER_API_URL


def get_user_data():
    response = requests.get(url)
    response_str_data = str(response.json())
    data = ['david', 'don', 'miriam']
    for each_value in data:
        match_info = re.findall(each_value.lower(), response_str_data.lower())
        if match_info:
            print("Match found and passed for : " + each_value)
        else:
            print("match not found : " + each_value)
            print(response.json())
            assert False, "Match not found"


def verify_response_notnull():
    response = requests.get(url)
    response_json = response.json()
    json_final_response = json.dumps(response, indent=4)
    dict_response = json.loads(json_final_response)
    for each_address_index in range(len(dict_response)):

        assert dict_response[each_address_index]['address']['geolocation']['lat'] is not None, "latitud value for address " + str(each_address_index)
        assert dict_response[each_address_index]['address']['geolocation']['long'] is not None, "long value for address " + str(each_address_index)


