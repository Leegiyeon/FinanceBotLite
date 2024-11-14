import unittest
from utils.api_handler import fetch_financial_products

class TestAPIHandler(unittest.TestCase):
    def test_fetch_financial_products(self):
        result = fetch_financial_products()
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()