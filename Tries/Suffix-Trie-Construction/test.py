import SuffixTrie
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = SuffixTrie.SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))

if __name__ == "__main__":
    unittest.main()