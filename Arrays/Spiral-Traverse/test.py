import spiralTraverse
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse.spiralTraverse(matrix), expected)


if __name__ == "__main__":
    unittest.main()