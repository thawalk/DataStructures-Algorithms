# time complexity: O(n^2) space complexity: O(1)

def selectionSort(array):
    firstIdx = 0
    lengthOfArray = len(array)
    while firstIdx < lengthOfArray - 1:
        smallestIdx = firstIdx
        for i in range(firstIdx, lengthOfArray):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(array, firstIdx, smallestIdx)
        firstIdx += 1
    return array
def swap(array, i , j):
    array[i], array[j] = array[j], array[i]