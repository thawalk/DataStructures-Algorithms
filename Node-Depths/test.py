import nodeDepths
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = nodeDepths.BinaryTree(1)
        root.left = nodeDepths.BinaryTree(2)
        root.left.left = nodeDepths.BinaryTree(4)
        root.left.left.left = nodeDepths.BinaryTree(8)
        root.left.left.right = nodeDepths.BinaryTree(9)
        root.left.right = nodeDepths.BinaryTree(5)
        root.right = nodeDepths.BinaryTree(3)
        root.right.left = nodeDepths.BinaryTree(6)
        root.right.right = nodeDepths.BinaryTree(7)
        actual = nodeDepths.nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__ == "__main__":
    unittest.main()