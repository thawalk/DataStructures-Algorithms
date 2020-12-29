# Time Complexity = O(n), where n is the length of the input array | Space Complexity = O(1)

def hasSingleCycle(array):
    counter = 0
    startIdx = 0
    currentIdx = startIdx
    while counter < len(array):
        if currentIdx == startIdx and counter > 0:
            return False
        counter += 1
        currentIdx = newIndex(array, currentIdx)
    return currentIdx == startIdx

def newIndex(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else (nextIdx + len(array))




