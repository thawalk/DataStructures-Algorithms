# time complexity: O(n^2) space complexity: O(1)
                    
def insertionSort(array):
    lastIdx = len(array) - 1
    currentIdx = 0
    while currentIdx < lastIdx:
        for i in range(currentIdx + 1):
            if array[currentIdx - i] > array[currentIdx - i + 1]:
                swap(array, currentIdx - i)
            else:
                break
        currentIdx += 1
    return array

def swap(array, idx):
    array[idx], array[idx + 1] = array[idx + 1], array[idx]
