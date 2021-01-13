import longestPalindromicSubstring
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestPalindromicSubstring.longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")

if __name__ == "__main__":
    unittest.main()