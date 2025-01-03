import unittest
from unittest.mock import patch
from src.utility import CustomUtils

class TestCustomUtils(unittest.TestCase):
    @patch("builtins.input", return_value="y")
    def test_confirm_action_yes(self, mock_input):
        result = CustomUtils.confirm_action("Test prompt?")
        self.assertTrue(result)

    @patch("builtins.input", return_value="n")
    def test_confirm_action_no(self, mock_input):
        result = CustomUtils.confirm_action("Test prompt?")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
