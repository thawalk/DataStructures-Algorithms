import findThreeLargestNumbers
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers.findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

if __name__ == "__main__":
    unittest.main()