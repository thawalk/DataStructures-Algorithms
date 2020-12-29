import productSum
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum.productSum(test), 12)

if __name__ == "__main__":
    unittest.main()