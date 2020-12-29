# <-------------------- Recursive ---------------------->

# Average Time Complexity = O(log(n)) | Average Space Complexity = O(log(n))
# Worst Time Complexity = O(n) | Worst Space Complexity = O(N)

# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if self.value > value:
#             if self.left is None:
#                 self.left = BST(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right is None:
#                 self.right = BST(value)
#             else:
#                 self.right.insert(value)
#         return self
    
#     def contains(self, value):
#         if self.value > value:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.contains(value)
#         elif self.value < value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.contains(value)
#         else:
#             return True

#     def remove(self, value, parent=None):
#         if value > self.value:
#             if self.right is not None:
#                 self.right.remove(value, self)
#         elif value < self.value:
#             if self.left is not None:
#                 self.left.remove(value, self)
#         else:
#             if self.left is not None and self.right is not None:
#                 self.value = self.right.getMinValue()
#                 self.right.remove(self.value, self)
#             elif parent is None:
#                 if self.left is not None:
#                     self.value = self.left.value
#                     self.right = self.left.right
#                     self.left = self.left.left
#                 elif self.right is not None:
#                     self.value = self.right.value
#                     self.left = self.right.left
#                     self.right = self.right.right
#                 else:
#                     pass
#             elif self == parent.left:
#                 parent.left = self.left if self.left is not None else self.right
#             elif self == parent.right:
#                 parent.right = self.right if self.right is not None else  self.left
#         return self

#     def getMinValue(self):
#         if self.left is None:
#             return self.value
#         else:
#             return self.left.getMinValue()



# <------------------------- Iterative ------------------------->

# Average Time Complexity = O(log(n)) | Average Space Complexity = O(1)
# Worst Time Complexity = O(n) | Worst Space Complexity = O(1)

class BST:
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None

    def insert(self, value):
        currentNode = self
        while True:
            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


    