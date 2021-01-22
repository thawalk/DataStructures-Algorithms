# <---------------- Approach 1 ---------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

def isMonotonic(array):
    nonDecreasing = True
    nonIncreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            nonIncreasing = False
        elif array[i] < array[i-1]:
            nonDecreasing = False
    return nonDecreasing or nonIncreasing

