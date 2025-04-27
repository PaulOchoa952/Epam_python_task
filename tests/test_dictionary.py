import unittest
import os
from io import StringIO
import sys
# Add the parent directory to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dictionary_task import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        # Create a new instance of Dictionary for each test
        self.dictionary = Dictionary()
        # Redirect stodout to capture print state
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout after each test
        sys.stdout = sys.__stdout__

    def test_new_entry(self):
        self.dictionary.newEntry("apple", "A red fruit")
        # Assert that the word is in the dictionary
        self.assertIn("apple", self.dictionary.words)
        self.assertEqual(self.dictionary.words["apple"], "A red fruit")

    def test_look_existing_word(self):
        # Add a word and look it up
        self.dictionary.newEntry("banana", "A yellow fruit")
        self.dictionary.look("banana")
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "The description for banana is: A yellow fruit")

    def test_look_non_existing_word(self):
        # Look up a word that doesn't exist
        self.dictionary.look("orange")
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "orange not found in the dictionary")


if __name__ == "__main__":
    unittest.main()
