# <------------ Iterative ------------->
# Time Complexity = O(N) | Space Complexity = O(N), for the queue, roughlty N/2

# def invertBinaryTree(tree):
#     queue = [tree]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current is None:
#             continue
#         swapLeftAndRight(current)
#         queue.append(current.left)
#         queue.append(current.right)

# def swapLeftAndRight(node):
#     node.left, node.right = node.right, node.left 

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.right = right
#         self.left = left

# <------------- Recursive -------------->
# Time Complexity = O(N) | Space Complexity = O(d)
# There is no queue in recursive approach

def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(node):
    node.left, node.right = node.right, node.left 

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = right
        self.left = left