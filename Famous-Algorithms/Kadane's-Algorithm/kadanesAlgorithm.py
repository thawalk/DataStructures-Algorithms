# Time Complexity = O(n) | Space Complexity = O(1) 

def kadanesAlgorithm(array):
    maxAtThisPoint = array[0]
    maxSoFar = array[0]
    for idx in range(1, len(array)):
        maxAtThisPoint = max(array[idx], maxAtThisPoint + array[idx])
        maxSoFar = max(maxSoFar, maxAtThisPoint)
    return maxSoFar
