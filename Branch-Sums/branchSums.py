class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def branchSums(root):
    ans = []
    branchSumsHelper(root, 0, ans)
    return ans

def branchSumsHelper(currentNode, value, ans):
    if currentNode is None:
        return
    
    value += currentNode.value
    if currentNode.left is None and currentNode.right is None:
        ans.append(value)
        return

    branchSumsHelper(currentNode.left, value, ans)
    branchSumsHelper(currentNode.right, value, ans)
