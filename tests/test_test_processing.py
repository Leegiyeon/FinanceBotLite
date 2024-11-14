import unittest
from utils.text_processing import analyze_question

class TestTextProcessing(unittest.TestCase):
    def test_analyze_question(self):
        question = "High-yield savings account recommendation"
        result = analyze_question(question)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()