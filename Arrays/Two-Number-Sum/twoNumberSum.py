# Time Complexity = O(n^2) | Space Complexity = O(1)

# def twoNumberSum(array, targetSum):
#     for i in array:
#         for j in array:
#             if i != j and (i + j) == targetSum:
#                  return [i, j]

# Time Complexity = O(n) | Space Complexity = O(n)

# def twoNumberSum(array, targetSum):
#     map = {}
#     for i in range(len(array)):
#         if (targetSum - array[i]) in map: 
#             return [array[i], targetSum - array[i]]
#         else: 
#             map[array[i]] = True 

# Time Complexity = O(nlogn) | Space Complexity = O(nlogn)

def twoNumberSum(array, targetSum):
    array = mergeSort(array)
    leftP = 0
    rightP = len(array) - 1
    while leftP != rightP:
        if (array[leftP] + array[rightP]) == targetSum:
            return [array[leftP], array[rightP]]
        elif (array[leftP] + array[rightP]) < targetSum:
            leftP += 1
        else: 
            rightP -= 1

def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray


