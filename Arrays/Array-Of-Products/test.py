import arrayOfProducts
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts.arrayOfProducts(array)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()