import logging
import unittest

from day2.python_solution import strategy_prediction

L = logging.getLogger(__name__)


class StrategyPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input", "r") as f:
            self.Strategy = f.readlines()

    def tearDown(self):
        self.Strategy = None

    def test_strategy_prediction(self):
        self.assertEqual(strategy_prediction(strategy_list=self.Strategy), 32)
        self.assertEqual(strategy_prediction(filename="./test/test_input"), 32)
