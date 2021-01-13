#  Time Complexity = O(n^2)| Space Complexity = O(n)

def threeNumberSum(array, targetSum):
    heapSort(array)
    ans = []
    for i in range(len(array) - 2):        
        currentIdx = i
        leftIdx = i + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            total = array[currentIdx] + array[leftIdx] + array[rightIdx]
            if total == targetSum:
                ans.append([array[currentIdx], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif total < targetSum:
                leftIdx += 1                
            elif total > targetSum: 
                rightIdx -= 1
    return ans

def heapSort(array):
    buildMaxHeap(array)
    for currentIndex in reversed(range(1, len(array))):
        swap(array, 0, currentIndex)
        siftDown(0,currentIndex - 1,array)


def buildMaxHeap(array):
    firstParentIndex = ((len(array) - 1) - 1)//2
    lastIdx = len(array) - 1
    for currentIndex in reversed(range(firstParentIndex + 1)):
        siftDown(currentIndex, lastIdx, array)

def children(currentIndex):
    childLeftIdx = (currentIndex * 2) + 1
    childRightIdx = (currentIndex * 2) + 2
    return childLeftIdx, childRightIdx

def siftDown(currentIndex, lastIdx, array):
    childLeftIdx, childRightIdx = children(currentIndex)
    while childLeftIdx <= lastIdx:
        if childRightIdx <= lastIdx and array[childLeftIdx] < array[childRightIdx]:
            idxToSwap = childRightIdx
        else:
            idxToSwap = childLeftIdx
        if array[currentIndex] < array[idxToSwap]:
            swap(array, currentIndex, idxToSwap)
            childLeftIdx, childRightIdx = children(idxToSwap)
        else:
            return 

def swap(array, i, j):
    array[i], array[j] = array[j], array[i] 