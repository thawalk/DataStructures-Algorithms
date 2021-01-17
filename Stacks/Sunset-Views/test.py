import sunsetViews
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews.sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()