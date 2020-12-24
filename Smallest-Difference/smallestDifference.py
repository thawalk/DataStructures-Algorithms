# Time Complexity = O(nlog(n) + mlog(m))| Space Complexity = O(nlog(n) + mlog(m))
# Space complexity is as such because of use of quickSort, if in place sort such as heap sort is used, it would be O(1)

def smallestDifference(arrayOne, arrayTwo):
    quickSort(arrayOne)
    quickSort(arrayTwo)
    lpOne, lpTwo = 0, 0
    smallestDiff = abs(arrayOne[lpOne] - arrayTwo[lpTwo])
    smallestPair = [arrayOne[lpOne], arrayTwo[lpTwo]]
    while lpOne < len(arrayOne) - 1 and lpTwo < len(arrayTwo) - 1:
        if arrayOne[lpOne] < arrayTwo[lpTwo]:
            lpOne += 1
        elif arrayOne[lpOne] > arrayTwo[lpTwo]:
            lpTwo += 1
        else:
            return [arrayOne[lpOne], arrayTwo[lpTwo]]
        if smallestDiff > abs(arrayOne[lpOne] - arrayTwo[lpTwo]):
            smallestPair = [arrayOne[lpOne], arrayTwo[lpTwo]]
            smallestDiff = abs(arrayOne[lpOne] - arrayTwo[lpTwo])
    return smallestPair


def quickSort(array):
    pivot = 0
    lastIdx = len(array) - 1
    quickSortHelper(array, pivot, lastIdx)

def quickSortHelper(array, pivot, lastIdx):
    if pivot >= lastIdx:
        return
    leftP = pivot + 1
    rightP = lastIdx
    while leftP <= rightP:
        if array[leftP] > array[pivot] and array[rightP] < array[pivot]:
            swap(array, leftP, rightP)
        if array[leftP] < array[pivot]:
            leftP += 1
        if array[rightP] > array[pivot]:
            rightP -= 1
    swap(array, pivot, rightP)
    leftSubArrayIsSmaller = (lastIdx - rightP + 1) > (rightP - 1 - pivot)
    if leftSubArrayIsSmaller:
        quickSortHelper(array, pivot, rightP - 1)
        quickSortHelper(array, rightP + 1, lastIdx)
    else:
        quickSortHelper(array, rightP + 1, lastIdx)
        quickSortHelper(array, pivot, rightP - 1)
        

def swap(array, i, j):
    array[i], array[j] = array[j], array[i] 
