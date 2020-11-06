# time complexity: O(n^2) space complexity: O(1)

def insertionSort(array):
    startIdx = 0
    lastIdx = len(array) - 1    
    while startIdx != lastIdx:
        if array[startIdx] > array[startIdx + 1]:
            for i in reversed(range(startIdx + 2)):
                if i > 0 and array[i] < array[i - 1]:
                    swap(i, i - 1, array)
                else:
                    break
        startIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
                    