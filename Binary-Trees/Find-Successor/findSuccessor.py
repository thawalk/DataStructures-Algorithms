class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# <------------- Approach 1 -------------->
# Time Complexity = O(n) | Space Complexity = O(n) 

# def findSuccessor(tree, node):
#     inOrderTraversalArray = inOrder(tree)
#     for idx in range(len(inOrderTraversalArray)):
#         if node == inOrderTraversalArray[idx] and idx != len(inOrderTraversalArray) - 1:
#             return inOrderTraversalArray[idx+1]
#     return None




# def inOrder(tree, array=[]):
#     if tree is None:
#         return 
    
#     inOrder(tree.left, array)
#     array.append(tree)
#     inOrder(tree.right, array)

#     return array


# <------------- Approach 2 -------------->
# Time Complexity = O(h), where h is the height of the tree | Space Complexity = O(1) 

def findSuccessor(tree, node):
    if node.right is None:
        return getParentNode(tree, node)
    return getLeftMostNode(node.right)

def getParentNode(tree, node):
    while node.parent is not None and node.parent.right == node:
        node = node.parent
    return node.parent

def getLeftMostNode(node):
    while node.left is not None:
        node = node.left
    return node
    






