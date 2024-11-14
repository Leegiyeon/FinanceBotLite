import unittest
import logging
from utils.text_processing import analyze_question

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestTextProcessing(unittest.TestCase):
    def test_analyze_question(self):
        question = "High-yield savings account recommendation"
        result = analyze_question(question)
        logger.info(f"Analysis result: {result}")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()