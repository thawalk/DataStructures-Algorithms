# <---------------------- Recursive --------------------------->

# Average Time Complexity = O(log(n))| Average Space Complexity = O(log(n))
# Worst Time Complexity = O(n)| Worst Space Complexity = O(n)

# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, tree.value)

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if tree.value < target:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     elif tree.value > target:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     else:
#         return closest

# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# <--------------------- Iterative ----------------------------->
# Average Time Complexity = O(log(n))| Average Space Complexity = O(1)
# Worst Time Complexity = O(n)| Worst Space Complexity = O(1)


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    while tree is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None