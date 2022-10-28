from pydoc import resolve
import pip._vendor.requests as requests
import unittest


class ApiTest(unittest.TestCase):

    global response_req
    response_req = requests.post(
        "https://www.google.com/recaptcha/api2/webworker.js?hl=en&v=ovmhLiigaw4D9ujHYlHcKKhP"
    )

    def test_StatusCode500(self):
        print(response_req.status_code)
        self.assertEqual(response_req.status_code, 500)

    def test_ContainsSQLError(self):
        self.assertIn("Sql error", response_req.text)


if __name__ == '__main__':
    unittest.main()
