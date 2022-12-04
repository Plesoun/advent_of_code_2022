import unittest

from day3.python_solution import split_compartments, calculate_priority


class BackpackPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day3", "r") as f:
            self.Backpacks = f.readlines()

    def test_split_compartments(self):
        self.assertEqual(split_compartments(self.Backpacks), [("vvMQnwwvrwWNfr", "tZJfppmSfJSmSg"), ("BzGqjlBqBB", "mztHNFzDHg")])

    def test_calculate_priority(self):
        self.assertEqual(calculate_priority([("vvMQnwwvrwWNfr", "tZJfppmSfJSmSg"), ("BzGqjlBqBB", "mztHNFzDHg")]), 32)