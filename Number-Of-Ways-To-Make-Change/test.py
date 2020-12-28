import numberOfWaysToMakeChange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange.numberOfWaysToMakeChange(6, [1, 5]), 2)

if __name__ == "__main__":
    unittest.main()