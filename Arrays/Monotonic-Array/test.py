import isMonotonic
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic.isMonotonic(array)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()