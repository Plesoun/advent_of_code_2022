import unittest

from day2.python_solution import strategy_prediction, strategy_prediction_p2


class StrategyPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day2", "r") as f:
            self.Strategy = f.readlines()

    def tearDown(self):
        self.Strategy = None

    def test_strategy_prediction_part_one(self):
        self.assertEqual(strategy_prediction(strategy_list=self.Strategy), 77)
        self.assertEqual(strategy_prediction(filename="./test/test_input_day2"), 77)
        with self.assertRaises(Exception):
            strategy_prediction()

    def test_strategy_prediction_p2(self):
        self.assertEqual(strategy_prediction_p2(strategy_list=self.Strategy), 73)
        self.assertEqual(strategy_prediction_p2(filename="./test/test_input_day2"), 73)
        with self.assertRaises(Exception):
            strategy_prediction()
