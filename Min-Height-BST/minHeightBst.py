#  Time Complexity = O(nlog(n)) | Space Complexity = O(n)

# def minHeightBst(array):
#     return constructMinHeightBST(array, None, 0, len(array) - 1)

# def constructMinHeightBST(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2 
#     valueToAdd = array[midIdx]
#     if bst is None:
#         bst = BST(valueToAdd)
#     else:
#         bst.insert(valueToAdd)
#     constructMinHeightBST(array, bst, startIdx, midIdx - 1)
#     constructMinHeightBST(array, bst, midIdx + 1, endIdx)
#     return bst

# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.right = None
#         self.left = None

#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = BST(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right is None:
#                 self.right = BST(value)
#             else:
#                 self.right.insert(value)

# <------------------- Better Time Complexity Below ----------------->

# Time Complexity = O(N) | Space Complexity = O(N) 

def minHeightBst(array):
    return constructMinHeightBST(array, None, 0, len(array) - 1)

def constructMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2 
    newBstNode = BST(array[midIdx])
    if bst is None:
        bst = newBstNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newBstNode
            bst = bst.left
        else:
            bst.right = newBstNode
            bst = bst.right
    constructMinHeightBST(array, bst, startIdx, midIdx - 1)
    constructMinHeightBST(array, bst, midIdx + 1, endIdx)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None