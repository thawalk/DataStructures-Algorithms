import maxSubsetSumNoAdjacent
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent.maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)

if __name__ == "__main__":
    unittest.main()