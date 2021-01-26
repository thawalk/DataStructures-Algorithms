import firstDuplicateValue
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValue.firstDuplicateValue(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()