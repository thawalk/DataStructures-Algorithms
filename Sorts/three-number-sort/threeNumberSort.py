# <------------------ Approach 1 ---------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

# def threeNumberSort(array, order):
#     # keep track of the counts
#     validCounts = [0,0,0]

#     # loop through the array and count as you go
#     for elem in array:
#         validCounts[order.index(elem)] += 1

#     # overwrite the current array with the values
#     for i in range(3):
#         value = order[i]
#         count = validCounts[i]

#         numberOfElements = sum(validCounts[:i])
#         for n in range(count):
#             currentIdx = numberOfElements + n
#             array[currentIdx] = value
#     return array            

# <------------------ Approach 2 ---------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

# def threeNumberSort(array, order):
#     firstIndex = 0
#     lastIdx = len(array) - 1

#     # forward pass to set the elements according to the first element in the order array
#     for i in range(len(array)):
#         if array[i] == order[0]:
#             array[firstIndex], array[i] = array[i], array[firstIndex]
#             firstIndex += 1

#     thirdIdx = lastIdx
#     # backward pass to set the elements according to the last element in the order array
#     for i in range(lastIdx, -1, -1):
#         if array[i] == order[2]:
#             array[thirdIdx], array[i] = array[i], array[thirdIdx]
#             thirdIdx -= 1

#     return array

# <------------------ Approach 3 ---------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

def threeNumberSort(array, order):
    firstValue, secondValue = order[0], order[1]
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

    while secondIdx <= thirdIdx:
        value = array[secondIdx]

        if value == firstValue:
            swap(firstIdx, secondIdx, array)
            firstIdx += 1
            secondIdx += 1
        elif value == secondValue:
            secondIdx += 1
        else:
            swap(secondIdx, thirdIdx, array)
            thirdIdx -= 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]




