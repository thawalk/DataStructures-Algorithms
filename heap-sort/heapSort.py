# time complexity: Best, O(nlog(n)) Average, O(nlog(n)) Worst, O(nlog(n))
#  space complexity: O(1)
def heapSort(array):
    buildMaxHeap(array)
    for i in reversed(range(1,len(array))):
        swap(0, i, array)
        siftDown(array, 0, i-1)
    return array

def buildMaxHeap(array):
    firstParentIdx = ((len(array) - 1) - 1) // 2
    lastIdx = len(array) - 1
    for i in reversed(range(firstParentIdx + 1)):
        siftDown(array, i, lastIdx)

def siftDown(array, currentIdx, lastIdx):
    childLeftIdx = (currentIdx * 2) + 1
    # print('hello I am getting called')
    # print(currentIdx)
    while childLeftIdx <= lastIdx:
        if ((currentIdx * 2) + 2) <= lastIdx:
            childRightIdx = (currentIdx * 2) + 2
        else:
            childRightIdx = -1
        
        if (childRightIdx != -1) and array[childRightIdx] > array[childLeftIdx]:
            idxToSwap = childRightIdx
        else:
            idxToSwap = childLeftIdx

        if array[currentIdx] < array[idxToSwap]:
            swap(currentIdx, idxToSwap, array)
            currentIdx = idxToSwap
            childLeftIdx = currentIdx * 2 + 1
        else:
            return

def swap(i,j, array):
    array[i], array[j] = array[j], array[i]