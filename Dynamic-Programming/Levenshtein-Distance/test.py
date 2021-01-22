import levenshteinDistance
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance.levenshteinDistance("abc", "yabd"), 2)
if __name__ == "__main__":
    unittest.main()