import minNumberOfCoins
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfCoins.minNumberOfCoinsForChange(7, [1, 5, 10]), 3)

if __name__ == "__main__":
    unittest.main()