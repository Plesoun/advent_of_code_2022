import unittest

from day4.python_solution import range_comparison


class CampCleanupTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day3", "r") as f:
            self.Backpacks = f.readlines()

    def test_range_comparison(self):
        self.assertTrue(range_comparison(range_1="1-5", range_2="3-4"))
        self.assertFalse(range_comparison(range_1="1-5", range_2="3-6"))
        self.assertFalse(range_comparison(range_1="1-5", range_2="6-8"))