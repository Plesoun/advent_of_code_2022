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
            "/btm": 282959,
            "/hmbbjbf": 275929,
            "/rhpwvff": 193293,
            "/zlpmfh.gpt": 191479,
            "/fmfnpm": [
                    "fgtqvq",
                    "rvnwwfq",
                    "wrzcjwc",
                    "zlpmfh"
                ],
            "/fmfnpm/fwdvgnqp.fsm": 194704,
            "/fmfnpm/fwdwq.tsq": 48823,
            "/fmfnpm/mtjngt": 224991,
            "/fmfnpm/rdsgpfjb.sfn": 79386,
        }
    
    
    def test_dir_enumerator(self):
        self.assertEqual(dir_enumerator(self.Input), self.StructureExample)
    
    
    def test_dir_sizer(self):
        pass
