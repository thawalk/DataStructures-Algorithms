# time complexity: worst: O(n^2) ave: O(nlog(n)),  space complexity: O(log(n))

def quickSort(array):
    startIdx = 0
    lastIdx = len(array) - 1
    quickSortHelper(array, startIdx, lastIdx)
    return array

def quickSortHelper(array, startIdx, lastIdx):
    if startIdx >= lastIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = lastIdx 
    while rightIdx >= leftIdx:
        if array[pivotIdx] < array[leftIdx] and array[pivotIdx] > array[rightIdx]:
            swap(leftIdx,rightIdx, array)
        elif array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        elif array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(rightIdx, pivotIdx, array)
    leftSubArraySmaller = (rightIdx - 1 - startIdx) < (lastIdx - rightIdx + 1)
    if leftSubArraySmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, lastIdx)
    else:
        quickSortHelper(array, rightIdx + 1, lastIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
        



def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

