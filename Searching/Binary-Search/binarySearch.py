# <----------- Iterative ------------->

# Time Complexity = O(log(n)) | Space Complexity = O(1) 

def binarySearch(array, target):
    leftP = 0
    rightP = len(array) - 1
    middleIdx = ((leftP + rightP)//2)
    while leftP <= rightP:
        middleIdx = (leftP + rightP) // 2
        if array[middleIdx] == target:
            return middleIdx
        elif array[middleIdx] > target:
            rightP = middleIdx - 1
        else:
            leftP = middleIdx + 1
    return -1

# <------------ Recursive --------------->

# Time Complexity = O(log(n))| Space Complexity = O(log(n)), frames on the call stack

# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)

# def binarySearchHelper(array, target, leftP, rightP):
#     if leftP > rightP:
#         return -1
#     middleIdx = ((leftP + rightP)//2)
#     if array[middleIdx] == target:
#         return middleIdx
#     elif array[middleIdx] > target:
#         return binarySearchHelper(array, target, leftP, middleIdx - 1)
#     else:
#         return binarySearchHelper(array, target, middleIdx + 1, rightP)

