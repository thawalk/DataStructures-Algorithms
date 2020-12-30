import caesarCipherEncryptor
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor.caesarCipherEncryptor("xyz", 2), "zab")

if __name__ == "__main__":
    unittest.main()