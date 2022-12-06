import unittest

from day6.python_solution import start_of_packet_filter


class SignalRecieverTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_signal_start(self):
        self.assertEqual(start_of_packet_filter("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(start_of_packet_filter("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)

        self.assertEqual(start_of_packet_filter("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(start_of_packet_filter("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)


