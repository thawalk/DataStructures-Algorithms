# def heapSort(array):
#     buildMaxHeap(array)

# def buildMaxHeap(array):
#     firstParentIdx = ((len(array) - 1) - 1) // 2
#     lastIdx = len(array) - 1
#     for i in reversed(range(firstParentIdx + 1)):
#         siftDown(array, i, lastIdx)

# def siftDown(array, parentIdx, lastIdx):
#     childLeftIdx = (parentIdx * 2) + 1