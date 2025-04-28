import unittest
from io import StringIO
import sys
from dictionary_task import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        # Create a new instance of Dictionary for each test
        self.dictionary = Dictionary()
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout after each test
        sys.stdout = sys.__stdout__

    def test_new_entry(self):
        # Mock user input for adding a new word
        inputs = iter(["apple", "A red fruit"])
        self.dictionary.new_Entry = lambda: self.dictionary.words.update({next(inputs): next(inputs)})
        self.dictionary.new_Entry()
        # Assert that the word is in the dictionary
        self.assertIn("apple", self.dictionary.words)
        self.assertEqual(self.dictionary.words["apple"], "A red fruit")

    def test_look_existing_word(self):
        # Add a word to the dictionary
        self.dictionary.words["banana"] = "A yellow fruit"
        # Mock user input for looking up the word
        self.dictionary.look = lambda: print(f"The description for 'banana' is: {self.dictionary.words['banana']}")
        self.dictionary.look()
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "The description for 'banana' is: A yellow fruit")

    def test_look_non_existing_word(self):
        # Mock user input for looking up a non-existing word
        self.dictionary.look = lambda: print("'orange' not found in the dictionary.")
        self.dictionary.look()
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the expected output
        self.assertEqual(output, "'orange' not found in the dictionary")


if __name__ == "__main__":
    unittest.main()