import unittest
from io import StringIO
import sys
from spend_task import newItem, get_Total, items_bought


class TestSpendTask(unittest.TestCase):
    def setUp(self):
        # Clear the items_bought list before each test
        items_bought.clear()
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout after each test
        sys.stdout = sys.__stdout__

    def test_new_item(self):
        # Add a new item to the list
        newItem("socks")
        # Assert that the item is added to the list
        self.assertIn("socks", items_bought)
        self.assertEqual(items_bought, ["socks"])

    def test_get_total_with_valid_items(self):
        # Add valid items to the list
        items_bought.extend(["socks", "shoes"])
        # Calculate the total with a tax of 10% (0.1)
        total = get_Total(0.1)
        # Assert the total is calculated correctly
        self.assertEqual(total, round((5 + 60) * 1.1, 2))  # (5 + 60) + 10% tax

    def test_get_total_with_invalid_items(self):
        # Add valid and invalid items to the list
        items_bought.extend(["socks", "hat"])  # "hat" is not in costs
        # Calculate the total with a tax of 5% (0.05)
        total = get_Total(0.05)
        # Assert the total is calculated correctly (ignoring "hat")
        self.assertEqual(total, round(5 * 1.05, 2))  # 5 + 5% tax

    def test_get_total_with_empty_list(self):
        # Ensure the list is empty
        self.assertEqual(items_bought, [])
        # Calculate the total with a tax of 10% (0.1)
        total = get_Total(0.1)
        # Assert the total is 0
        self.assertEqual(total, 0)

    def test_output_for_valid_items(self):
        # Add valid items to the list
        items_bought.extend(["socks", "shoes"])
        # Calculate the total with a tax of 10% (0.1)
        get_Total(0.1)
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the output contains the correct messages
        self.assertIn("socks exists in the dictionary", output)
        self.assertIn("shoes exists in the dictionary", output)
        self.assertIn("The total is:", output)

    def test_output_for_invalid_items(self):
        # Add valid and invalid items to the list
        items_bought.extend(["socks", "hat"])  # "hat" is not in costs
        # Calculate the total with a tax of 5% (0.05)
        get_Total(0.05)
        # Capture the printed output
        output = self.held_output.getvalue().strip()
        # Assert the output contains the correct messages
        self.assertIn("socks exists in the dictionary", output)
        self.assertIn("hat doesnt exist in the dictionary", output)
        self.assertIn("The total is:", output)


if __name__ == "__main__":
    unittest.main()
