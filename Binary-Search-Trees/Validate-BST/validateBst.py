# Time Complexity = O(n) | Space Complexity = O(d)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(currentNode, minValue, maxValue):
    if currentNode is None:
        return True
    if currentNode.value >= maxValue or currentNode.value < minValue:
        return False
    return validateBstHelper(currentNode.right, currentNode.value, maxValue) and validateBstHelper(currentNode.left, minValue ,currentNode.value)
