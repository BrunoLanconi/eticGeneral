import unittest
from unittest.mock import Mock, patch

from src.modules.add import add


class TestAdd(unittest.TestCase):
    """
    A test case for the add function.

    Methods:
        - setUp: Set up the test case.
        - tearDown: Tear down the test case.
        - test_add: Test the add function.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        print("Setting up test case...")

    def tearDown(self):
        """
        Tear down the test case.
        """
        print("Tearing down test case...")

    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)

    def test_mock_add(self):
        """
        Test the add function with a mock.
        """
        mock_add = Mock(return_value=3)

        self.assertEqual(mock_add(), 3)
        self.assertEqual(mock_add.call_count, 1)

    @patch("src.modules.add", return_value=3)
    def test_mock_add_with_patch(self, mock_add: Mock):
        """
        Test the add function with a mock and patch.
        """
        self.assertEqual(mock_add(), 3)
        self.assertEqual(mock_add.call_count, 1)

    def test_add_expected_failure(self):
        """
        Test the add function with an expected failure.
        """
        with self.assertRaises(TypeError):
            add("1", 2)  # type: ignore

    def test_add_expected_failure_with_message(self):
        """
        Test the add function with an expected failure and message.
        """
        with self.assertRaisesRegex(TypeError, "can only concatenate str"):
            add("1", 2)  # type: ignore


if __name__ == "__main__":
    unittest.main()
