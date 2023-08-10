import json
import requests
from jsonschema import validate

from API_Assignment.Test_Data.Config import ConfigItems
from API_Assignment.Utility.LogDetails import LogDetails

url = ConfigItems.CART_API_URL
logging = LogDetails.getLogger(ConfigItems.LOGGER_PATH)


def response_schema():
    logging.info("Fetching data from the API...")
    response = requests.get(url)
    assert response.status_code == 200
    logging.info("API response received successfully.")
    response_data = response.json()
    json_final_response = json.dumps(response_data, indent=4)
    logging.debug("Formatted JSON response:\n%s", json_final_response)
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
        logging.info("Validating response schema...")
        validate(instance=json_final_response, schema=response_schema)
        logging.info("Response schema validation successful.")

    except Exception as e:
        print("Response schema validation is failed " + str(e))
        logging.error("Response schema validation failed: %s", str(e))


def product_fields():
    logging.info("Fetching data from the API...")
    response = requests.get(url)
    response_data = response.json()
    logging.info("API response received successfully.")
    for cart in response_data:
        for product in cart["products"]:
            assert "productId" in product, "productId is missing in a product."
            assert product["productId"] is not None, "productId is null in a product."

            assert "quantity" in product, "quantity is missing in a product."
            assert product["quantity"] is not None, "quantity is null in a product."
            logging.debug("Validating product: productId=%s, quantity=%s",
                          product.get("productId"), product.get("quantity"))
