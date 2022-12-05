import unittest

from day4.python_solution import complete_overlap, partial_overlap


class CampCleanupTestCase(unittest.TestCase):

    def test_complete_overlap(self):
        self.assertTrue(complete_overlap(range_1="1-5", range_2="3-4"))
        self.assertTrue(complete_overlap(range_1="63-64", range_2="13-64"))
        self.assertFalse(complete_overlap(range_1="1-5", range_2="3-6"))
        self.assertFalse(complete_overlap(range_1="1-5", range_2="6-8"))

    def test_partial_overlap(self):
        self.assertTrue(partial_overlap(range_1="1-5", range_2="3-4"))
        self.assertTrue(partial_overlap(range_1="63-64", range_2="13-64"))
        self.assertTrue(partial_overlap(range_1="1-5", range_2="3-6"))
        self.assertTrue(partial_overlap(range_1="3-6", range_2="1-5"))
        self.assertFalse(partial_overlap(range_1="1-5", range_2="6-8"))
        self.assertFalse(partial_overlap(range_1="6-8", range_2="1-5"))