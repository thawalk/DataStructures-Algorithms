# time complexity: worst: O(n^2) ave: O(nlog(n)),  space complexity: O(log(n))

def quickSort(array):
    firstIdx = 0
    lastIdx = len(array) - 1
    quickSortHelper(firstIdx, lastIdx, array)
    return array

def quickSortHelper(firstIdx, lastIdx, array):
    if firstIdx >= lastIdx:
        return
    pivot = firstIdx
    leftP = firstIdx + 1
    rightP = lastIdx
    while leftP < rightP:
        if array[leftP] > array[pivot] and array[rightP] < array[pivot]:
            swap(array, leftP, rightP)
        if array[leftP] <= array[pivot]:
            leftP += 1
        if array[rightP] >= array[pivot]:
            rightP -=1
    swap(array, rightP, pivot)
    leftSubArrayIsSmaller = (rightP - 1 - firstIdx) < (lastIdx - rightP + 1)
    if leftSubArrayIsSmaller:
        quickSortHelper(firstIdx, rightP - 1, array)
        quickSortHelper(rightP + 1, lastIdx, array)
    else:
        quickSortHelper(rightP + 1, lastIdx, array)
        quickSortHelper(firstIdx, rightP - 1, array)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]