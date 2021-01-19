class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    inOrderTraversalArray = inOrder(tree)
    for idx in range(len(inOrderTraversalArray)):
        if node == inOrderTraversalArray[idx] and idx != len(inOrderTraversalArray) - 1:
            return inOrderTraversalArray[idx+1]
    return None




def inOrder(tree, array=[]):
    if tree is None:
        return 
    
    inOrder(tree.left, array)
    array.append(tree)
    inOrder(tree.right, array)

    return array


