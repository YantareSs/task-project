import unittest
from task_app import validate_priority


class TestPriority(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_priority("high"), "high")
        self.assertEqual(validate_priority("low"), "low")
        self.assertEqual(validate_priority("normal"), "normal")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            validate_priority("urgent")


if __name__ == "__main__":
    unittest.main()
