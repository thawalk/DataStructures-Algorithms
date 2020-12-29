import selectionSort
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selectionSort.selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == '__main__':
    unittest.main()