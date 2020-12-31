class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    

    # Time Complexity = O(n) amortized analysis | Space Complexity = O(1)
    def buildHeap(self, array):
        firstParentNodeIdx = ((len(array) - 1) - 1) // 2
        lastIdx = len(array) - 1
        for currentNodeIdx in reversed(range(firstParentNodeIdx + 1)):
            self.siftDown(currentNodeIdx, lastIdx, array)
        print(array)
        return array

    def children(self, idx):
        childLeft = (2*idx) + 1
        childRight = (2*idx) + 2
        return childLeft, childRight

    # Time Complexity = O(log(n)) | Space Complexity = O(1)
    def siftDown(self, currentNodeIdx, lastIdx, array):
        childLeftIdx, childRightIdx = self.children(currentNodeIdx)
        while childLeftIdx <= lastIdx:
            if childRightIdx <= lastIdx and array[childRightIdx] < array[childLeftIdx]:  
                idxToSwap = childRightIdx
            else: 
                idxToSwap = childLeftIdx 
            if array[idxToSwap] < array[currentNodeIdx]:
                self.swap(idxToSwap, currentNodeIdx, array)
                currentNodeIdx = idxToSwap
                childLeftIdx, childRightIdx = self.children(currentNodeIdx)
            else:
                return

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) -1, self.heap)
        return valueToRemove

    # Time Complexity = O(log(n)) | Space Complexity = O(1)
    def siftUp(self, currentNodeIdx):
        parentNodeIdx = (currentNodeIdx - 1) // 2
        while currentNodeIdx > 0 and self.heap[currentNodeIdx] < self.heap[parentNodeIdx]:
            self.swap(currentNodeIdx, parentNodeIdx, self.heap)
            currentNodeIdx = parentNodeIdx
            parentNodeIdx = (currentNodeIdx - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        self.siftUp((len(self.heap) - 1))

