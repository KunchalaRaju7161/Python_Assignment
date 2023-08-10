import json
import re
import requests
from jsonschema import validate

from API_Assignment.Test_Data.Config import ConfigItems

url = ConfigItems.CART_API_URL


def response_schema():
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    json_final_response = json.dumps(response_data, indent=4)
    print(json_final_response)
    response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "userId": {"type": "integer"},
            "date": {"type": "string", "format": "date-time"},
            "products": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "productId": {"type": "integer"},
                        "quantity": {"type": "integer"}
                    },
                    "required": ["productId", "quantity"]
                }
            },
            "__v": {"type": "integer"}
        },
        "required": ["id", "userId", "date", "products", "__v"]
    }
    }

    try:
        validate(instance=json_final_response, schema=response_schema)
    except Exception as e:
        print("Response schema validation is failed " + str(e))


def product_fields():
    response = requests.get(url)
    response_data = response.json()
    for cart in response_data:
        for product in cart["products"]:
            assert "productId" in product, "productId is missing in a product."
            assert product["productId"] is not None, "productId is null in a product."

            assert "quantity" in product, "quantity is missing in a product."
            assert product["quantity"] is not None, "quantity is null in a product."
