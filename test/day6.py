import unittest

from day6.python_solution import start_of_packet_filter


class SignalRecieverTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_signal_start(self):
        self.assertEqual(start_of_packet_filter("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)