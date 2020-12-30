import binarySearch
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
if __name__ == "__main__":
    unittest.main()