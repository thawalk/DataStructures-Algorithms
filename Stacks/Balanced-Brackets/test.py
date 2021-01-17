import balancedBrackets
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets.balancedBrackets("([])(){}(())()()"), True)
    
if __name__ == "__main__":
    unittest.main()