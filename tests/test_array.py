import unittest
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from array_task import get_the_word

class TestGetTheWord(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout after each test
        sys.stdout = sys.__stdout__

    def test_get_the_word(self):
        # Call the function
        get_the_word()
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "yes")

    def test_get_the_word_with_custom_value(self):
        # Call the function with a custom starting value
        get_the_word(value="start-")
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "start-yes")

if __name__ == "__main__":
    unittest.main()