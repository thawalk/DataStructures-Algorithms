import smallestDifference
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

if __name__ == '__main__':
    unittest.main()