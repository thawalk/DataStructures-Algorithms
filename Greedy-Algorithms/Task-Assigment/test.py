import taskAssignment
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[4, 2], [0, 5], [3, 1]]
        actual = taskAssignment.taskAssignment(k, tasks)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()