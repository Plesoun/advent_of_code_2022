import logging
import unittest

from day2.python_solution import strategy_prediction

L = logging.getLogger(__name__)


class StrategyPredictionTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input", "r") as f:
            self.Problem = f.readlines()
        print(self.Problem)

    def tearDown(self):
        self.Problem = None


    def test_strategy_prediction(self):
        self.assertEqual(strategy_prediction(), 27)