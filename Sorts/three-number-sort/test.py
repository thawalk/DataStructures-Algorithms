import threeNumberSort
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
        actual = threeNumberSort.threeNumberSort(array, order)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()