import unittest

from day7.python_solution import dir_enumerator, dir_sizer


class OutOfSpaceTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day7", "r") as f:
            self.Input = f.readlines()

        self.StructureExample = {
            "/": [
                    "fmfnpm",
                    "gwlwp",
                    "hchp",
                    "nsphznf",
                    "phschqg",
                    "spfwthmd",
                    "wchdqb",
                    "zlpmfh"
                ],
            "/_size": [282959, 275929, 193293, 191479],
            "/fmfnpm": [
                    "fgtqvq",
                    "rvnwwfq",
                    "wrzcjwc",
                    "zlpmfh"
                ],
            "/fmfnpm_size": [194704, 48823, 224991, 79386]
        }
    
    
    def test_dir_enumerator(self):
        self.assertEqual(dir_enumerator(self.Input), self.StructureExample)
    
    
    def test_dir_sizer(self):
        self.assertEqual(dir_sizer(self.StructureExample), 1491564)
