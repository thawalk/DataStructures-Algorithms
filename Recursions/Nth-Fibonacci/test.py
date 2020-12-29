import nthFibonacci
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(nthFibonacci.getNthFib(6), 5)
if __name__ == '__main__':
    unittest.main()