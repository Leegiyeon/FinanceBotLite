import unittest
import logging
from utils.api_handler import fetch_financial_products

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAPIHandler(unittest.TestCase):
    def test_fetch_financial_products(self):
        result = fetch_financial_products()
        logger.info(f"Fetched Data: {result}")
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()