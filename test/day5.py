import unittest

from day5.python_solution import crane_rearrange_step


class CraneRearrangeTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day5", "r") as f:
            self.Moves = f.readlines()

        self.StartingPoint = {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }

        self.Final = {
            1: ["C"],
            2: ["M"],
            3: ["P", "D", "N", "Z"]
        }

    def test_crane_rearrange_step(self):
        final = self.StartingPoint
        for move in self.Moves:
            final = crane_rearrange_step(move, final)
        self.assertEqual(final, self.Final)