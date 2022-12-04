import unittest

from day3.python_solution import split_compartment, find_intersection, calculate_priority


class BackpackPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day3", "r") as f:
            self.Backpacks = f.readlines()

    def test_split_compartment(self):
        self.assertEqual(split_compartment(self.Backpacks[0]), ("vvMQnwwvrwWNfr", "tZJfppmSfJSmSg"))
        self.assertEqual(split_compartment(self.Backpacks[1]), ("BzGqjlBqBB", "mztHNFzDHg"))

    def test_find_intersection(self):
        self.assertEqual(find_intersection(("vvMQnwwvrwWNfr", "tZJfppmSfJSmSg")), {"f"})
        self.assertEqual(find_intersection(("BzGqjlBqBB", "mztHNFzDHg")), {"z"})


    def test_calculate_priority(self):
        self.assertEqual(calculate_priority({"a"}), 1)
        self.assertEqual(calculate_priority({"B"}), 28)