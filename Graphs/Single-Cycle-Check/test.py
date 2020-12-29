import singleCycleCheck
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(singleCycleCheck.hasSingleCycle([2, 3, 1, -4, -4, 2]), True)

if __name__ == "__main__":
    unittest.main()