import moveElementToEnd
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd.moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

if __name__ == '__main__':
    unittest.main()