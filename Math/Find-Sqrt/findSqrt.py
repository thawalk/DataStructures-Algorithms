# Time Complexity = O(log(n)) | Space Complexity = O(log(n))

def findSqrt(n):
    answer = binarySearch(0, n, n)
    print(answer)

def binarySearch(lowerLimit, upperLimit, n):
    middle = (upperLimit + lowerLimit) // 2
    if middle * middle == n:
        return middle
    if lowerLimit >= upperLimit:
        return None
    if (middle * middle) > n:
        upperLimit = middle
        return binarySearch(lowerLimit, upperLimit,  n)
    else:
        return binarySearch(middle, upperLimit, n)