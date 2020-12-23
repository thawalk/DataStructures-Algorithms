# time complexity: Best, O(nlog(n)) Average, O(nlog(n)) Worst, O(nlog(n))
#  space complexity: O(1)

def heapSort(array):
    buildMaxHeap(array)
    for currentIdx in reversed(range(1, len(array))):
        swap(array, 0, currentIdx)
        siftDown(0, currentIdx - 1, array)
    return array


def buildMaxHeap(array):
    firstParentIdx = ((len(array) - 1) - 1) // 2
    lastIdx = len(array) - 1
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, lastIdx, array)

def children(parentIdx):
    childLeft =  (parentIdx * 2) + 1
    childRight = (parentIdx * 2) + 2
    return childLeft, childRight

def siftDown(parentIdx, lastIdx, array):
    childLeftIdx, childRightIdx = children(parentIdx)
    while childLeftIdx <= lastIdx:
        if childRightIdx <= lastIdx and array[childLeftIdx] < array[childRightIdx]:
            idxToSwap = childRightIdx
        else:
            idxToSwap = childLeftIdx
        if array[idxToSwap] > array[parentIdx]:
            swap(array, idxToSwap, parentIdx)
            parentIdx = idxToSwap
            childLeftIdx, childRightIdx = children(parentIdx)
        else:
            return

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
