import unittest

from day7.python_solution import dir_enumerator, dir_sizer


class OutOfSpaceTestCase(unittest.TestCase):
    def setUp(self):
        with open("./test/test_input_day7_2", "r") as f:
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
            "/fmfnpm_size": [48823, 194704, 224991, 79386],
            "/fmfnpm/fgtqvq_size": [293783, 324635],
            "/fmfnpm/rvnwwfq_size": [76914],
            "/fmfnpm/wrzcjwc": ["fwdwq", "lddhdslh", "mjp", ],
            "/fmfnpm/rvnwwfq_size": [196284, 284475, 2159],
        }
    
    
    def test_dir_enumerator(self):
        self.assertEqual(dir_enumerator(self.Input), self.StructureExample)
    
    
    def test_dir_sizer(self):
        self.assertEqual(dir_sizer(self.StructureExample, 100000), 48823)
