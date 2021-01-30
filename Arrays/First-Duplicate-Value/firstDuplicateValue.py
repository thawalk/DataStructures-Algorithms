# <--------- Approach 1 brute-force ----------->
# Time Complexity = O(n^2) | Space Complexity = O(1)

def firstDuplicateValue(array):
    minSecondIdx = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minSecondIdx = min(minSecondIdx, j)
    return array[minSecondIdx] if minSecondIdx != len(array) else -1
            
# <--------- Approach 2 using hashset ----------->
# Time Complexity = O(n) | Space Complexity = O(n)
 
def firstDuplicateValue(array):
    seen = set()
    for elem in array:
        if elem in seen:
            return elem
        seen.add(elem)
    return -1

# <--------- Approach 3 using negative values ----------->
# Time Complexity = O(n) | Space Complexity = O(1)

def firstDuplicateValue(array):
    for elem in array:
        if array[abs(elem) - 1] < 0:
            return elem
        array[abs(elem) - 1] = -(array[abs(elem) - 1])
    return -1

def ways(total, k):
    array = [[0 for i in range()]]