import sys
import os
import unittest

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quotes import load_quotes

class TestQuotes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_csv_path = 'quotes.csv'  # Ensure this path is correct for your setup

    def test_load_quotes(self):
        quotes = load_quotes(self.test_csv_path)
        self.assertIsInstance(quotes, list)
        self.assertGreater(len(quotes), 0)  # Assuming there are quotes in the file

if __name__ == '__main__':
    unittest.main()
