import unittest

from day4.python_solution import func_placeholder


class CampCleanupTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day3", "r") as f:
            self.Backpacks = f.readlines()

    def test_something(self):
        pass