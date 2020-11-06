# time complexity: O(n^2) space complexity: O(1)

def bubbleSort(array):
    counter = 0
    lastIdx = len(array) - 1
    stopLoop = False
    while stopLoop == False:
        stopLoop = True
        for i in range(lastIdx-counter):
            if(array[i] > array[i+1]):
                swap(i,i+1,array)
                stopLoop = False
        counter += 1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]    