import unittest

from day3.python_solution import split_compartments, calculate_priority


class StrategyPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day3", "r") as f:
            self.Strategy = f.readlines()

    def test_split_compartments(self):
        self.assertEqual(split_compartments(), ["sdjk", "LASdfhef"])

    def test_calculate_priority(self):
        self.assertEqual(calculate_priority(), 30)