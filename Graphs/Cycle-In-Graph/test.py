import cycleInGraph
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1, 3],
            [2, 3, 4],
            [0],
            [],
            [2, 5],
            []
        ]
        expected = True
        actual = cycleInGraph.cycleInGraph(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()