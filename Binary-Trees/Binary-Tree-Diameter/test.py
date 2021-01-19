import binaryTreeDiameter
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = binaryTreeDiameter.BinaryTree(1)
        root.left = binaryTreeDiameter.BinaryTree(3)
        root.left.left = binaryTreeDiameter.BinaryTree(7)
        root.left.left.left = binaryTreeDiameter.BinaryTree(8)
        root.left.left.left.left = binaryTreeDiameter.BinaryTree(9)
        root.left.right = binaryTreeDiameter.BinaryTree(4)
        root.left.right.right = binaryTreeDiameter.BinaryTree(5)
        root.left.right.right.right = binaryTreeDiameter.BinaryTree(6)
        root.right = binaryTreeDiameter.BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter.binaryTreeDiameter(root)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
