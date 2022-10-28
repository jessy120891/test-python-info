import pip._vendor.requests as requests
import unittest
from jsonschema import validate
from datetime import datetime, timedelta


class ApiTest(unittest.TestCase):

    global response_req
    today_date = datetime.now()
    next_date = datetime.now() + timedelta(1)
    response_req = requests.get(
        f'https://ct.pinterest.com/user/?event=search&ed=%7B%22np%22%3A%22gtm%22%7D&tid={today_date.timestamp()}&cb={next_date.timestamp()}'
    )

    def test_StatusCode200(self):
        self.assertEqual(response_req.status_code, 200)

    def test_read_one_operation_has_expected_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "aemEnabled": {
                    "type": "boolean"
                },
                "aemFnLnEnabled": {
                    "type": "boolean"
                },
                "aemPhEnabled": {
                    "type": "boolean"
                },
                "aemGeEnabled": {
                    "type": "boolean"
                },
                "aemDbEnabled": {
                    "type": "boolean"
                },
                "aemLocEnabled": {
                    "type": "boolean"
                },
                "ctEpikIframeEnabled": {
                    "type": "boolean"
                },
                "chromeNewUserAgentEnabled": {
                    "type": "boolean"
                },
                "isEu": {
                    "type": "boolean"
                },
                "isUtilizingAdvertiser1pEnabled": {
                    "type": "boolean"
                },
                "mdFrequency": {
                    "type": "number"
                },
                "ecmOriginTrialToken": {
                    "type": "string"
                },
                "piaaEndPoint": {
                    "type": "string"
                }
            },
        }

        validate(instance=response_req.json(), schema=schema)

    def test_BodyParameters(self):
        print(response_req.json()["isUtilizingAdvertiser1pEnabled"])
        self.assertFalse(response_req.json()["isUtilizingAdvertiser1pEnabled"])


if __name__ == '__main__':
    unittest.main()
