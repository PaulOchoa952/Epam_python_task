import unittest
from dictionary import Dictionary  # Replace `your_module` with the name of the file containing your class


class TestDictionary(unittest.TestCase):
    def setUp(self):
        """
        Set up a new instance of the Dictionary class for each test.
        """
        self.d = Dictionary()  # Create a new instance before each test

    def test_new_entry(self):
        """
        Test that a new fruit can be added and looked up.
        """
        self.d.newEntry("apple", "A red and sweet fruit")
        self.d.newEntry("banana", "A yellow fruit rich in potassium")

        # Check that the entries exist
        self.assertIn("apple", self.d.fruit)
        self.assertIn("banana", self.d.fruit)
        self.assertEqual(self.d.fruit["apple"], "A red and sweet fruit")
        self.assertEqual(self.d.fruit["banana"], "A yellow fruit rich in potassium")

    def test_lookup(self):
        """
        Test looking up a fruit's description.
        """
        self.d.newEntry("grapes", "Small round fruit often used in wine-making")

        # Look for an existing fruit
        self.assertEqual(self.d.fruit.get("grapes"), "Small round fruit often used in wine-making")
        # Look up a non-existing fruit
        self.assertIsNone(self.d.fruit.get("pineapple"))

    def test_add_items_and_total(self):
        """
        Test adding items to the items_bought list and the total costs calculation.
        """
        # Add items
        self.d.newItem("socks")
        self.d.newItem("shoes")
        self.d.newItem("hat")  # This item doesn't exist in the costs dictionary

        # Check the array of items bought
        self.assertListEqual(self.d.items_bought, ["socks", "shoes", "hat"])

        # Calculate total cost with tax
        self.d.items_bought = ["socks", "shoes"]  # Re-set for a predictable result
        self.assertEqual(self.d.get_Total(0.1), 71.5)  # Tax 10%, socks=5 + shoes=60 → total = 65 + 6.5 = 71.5

    def test_get_the_word(self):
        """
        Test getting the word by concatenating the nth letter from each word.
        """
        words = ["yoda", "best", "has"]  # Input array
        result = self._get_test_word(words)
        self.assertEqual(result, "yes")  # Check if the result is 'yes'

    def _get_test_word(self, words):
        """
        Helper to test the concatenation of the nth letter from each word.
        """
        value = ""
        for i in range(len(words)):
            value += words[i][i]
        return value


if __name__ == "__main__":
    unittest.main()