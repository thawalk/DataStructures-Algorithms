# <------------------------ Iterative ----------------->
# Time Complexity = O(N) | Space Complexity = O(h), where h is the height of the tree 

# def nodeDepths(root):
#     total = 0 
#     stack = [{"node": root, "depth": 0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo["node"], nodeInfo["depth"]
#         if node is None:
#             continue
#         total += depth
#         stack.append({"node": node.left, "depth": depth + 1})
#         stack.append({"node": node.right, "depth": depth + 1})    
#     return total

# <------------------------ Iterative ----------------->
# Time Complexity = O(N) | Space Complexity = O(h), where h is the height of the tree 
 
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
