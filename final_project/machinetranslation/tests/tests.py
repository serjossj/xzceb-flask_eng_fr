import unittest
from translator import english_to_french, french_to_english

# TASK 2 - translation_unittests


class TestTranslator(unittest.TestCase):
    def test_null_input_f2e(self):
        self.assertIsNone(french_to_english(None))

    def test_null_input_e2f(self):
        self.assertIsNone(english_to_french(None))
            
    def test_empty_input_f2e(self):
        self.assertIsNone(french_to_english(""))

    def test_empty_input_e2f(self):
        self.assertIsNone(english_to_french(""))

    def test_input_e2f(self):
        self.assertIn("Bonjour", english_to_french("Hello"))

    def test_input_f2e(self):
        self.assertIn("Hello", french_to_english("Bonjour"))


if __name__ == "__main__":
    unittest.main()
