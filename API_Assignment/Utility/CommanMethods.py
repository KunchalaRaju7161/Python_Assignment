import json
from jsonschema import validate

from API_Assignment.Test_Data.Config import ConfigItems


def validate_schema(responce, json_schema):
    result = validate(responce, json_schema)


def read_dataFrom_json(Path):
    with open(Path) as inputFile:
        jsonData = json.load(inputFile)
    return jsonData


def read_registerData():
    Path = ConfigItems.INPUT_JSON
    return read_dataFrom_json(Path)


def read_registeredData():
    Path = ConfigItems.REGISTERED_JSON
    return read_dataFrom_json(Path)


def extract_id():
    payload = read_registeredData()['user']
    key_to_extract = {'_id'}
    id = {key: payload[key] for key in payload.keys()}
    return id.get('_id')

def extract_token():
    payload = read_registeredData()['token']
    return payload


def write_jsonData(parsed_response):
    with open(ConfigItems.REGISTERED_JSON, 'w') as json_file:
        json.dump(parsed_response, json_file)


def write_jsonDataNew(parsed_response):
    with open(ConfigItems.REGISTERED_JSON, 'r+') as json_file:
        json.dump(parsed_response, json_file)
        file_data = json.load(json_file)
        file_data.append(parsed_response)
        json.dumps(file_data.json_file)


def extractmailandpass(payload):
    key_to_extract = {'password', 'email'}
    return {key: payload[key] for key in payload.keys() & key_to_extract}


def extractfromDic(payload, key):
    key_to_extract = {key}
    return {key: payload[key] for key in payload.keys() & key_to_extract}


def jsonParse(response):
    return response.json()
