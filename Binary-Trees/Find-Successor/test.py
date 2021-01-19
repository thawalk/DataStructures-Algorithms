import findSuccessor
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = findSuccessor.BinaryTree(1)
        root.left = findSuccessor.BinaryTree(2)
        root.left.parent = root
        root.right = findSuccessor.BinaryTree(3)
        root.right.parent = root
        root.left.left = findSuccessor.BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = findSuccessor.BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = findSuccessor.BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = findSuccessor.findSuccessor(root, node)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()