# time complexity: O(n^2) space complexity: O(1)

def selectionSort(array):
    firstIdx = 0
    lastIdx = len(array) - 1
    lenOfArray = len(array)
    while firstIdx != lastIdx:
        smallestIdx = firstIdx
        for i in range(firstIdx + 1, lenOfArray):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(firstIdx, smallestIdx, array)
        firstIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]