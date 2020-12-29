# time complexity: O(n^2) space complexity: O(1)

def bubbleSort(array):
    idx = 0
    lastIdx = len(array) - 1
    isSorted = False
    while not isSorted:
        isSorted = True
        while idx != lastIdx:
            if array[idx] > array[idx + 1]:
                swap(array, idx)
                isSorted = False
            idx += 1
        idx = 0
        lastIdx -= 1
    return array


def swap(array, idx):
    array[idx], array[idx+1] = array[idx+1], array[idx]
