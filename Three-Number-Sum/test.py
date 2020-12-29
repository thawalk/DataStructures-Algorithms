import threeNumberSum
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum.threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

if __name__ == '__main__':
    unittest.main()