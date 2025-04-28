import unittest
from unittest.mock import patch
from io import StringIO
from dictionary_task import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        # Create a new instance of Dictionary for each test
        self.dictionary = Dictionary()

    def test_new_entry(self):
        with patch('builtins.input', side_effect=["apple", "A red fruit"]):
            # Test adding a new entry
            self.dictionary.new_Entry()
        
        # Assert that the word is in the dictionary
        self.assertIn("apple", self.dictionary.words)
        self.assertEqual(self.dictionary.words["apple"], "A red fruit")

    def test_look_existing_word(self):
        # Prepopulate the dictionary with a word
        self.dictionary.words["banana"] = "A yellow fruit"
        
        with patch('builtins.input', side_effect=["banana"]), patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            # Test looking up an existing word
            self.dictionary.look()

            # Capture the printed output
            output = mocked_stdout.getvalue().strip()

        # Assert the expected output
        self.assertEqual(output, "The description for 'banana' is: A yellow fruit")

    def test_look_non_existing_word(self):
        with patch('builtins.input', side_effect=["orange"]), patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            # Test looking up a non-existing word
            self.dictionary.look()

            # Capture the printed output
            output = mocked_stdout.getvalue().strip()

        # Assert the expected output
        self.assertEqual(output, "'orange' not found in the dictionary.")


if __name__ == "__main__":
    unittest.main()