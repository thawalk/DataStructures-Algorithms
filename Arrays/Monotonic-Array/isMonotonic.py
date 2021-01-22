# <---------------- Approach 1 ---------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

# def isMonotonic(array):
#     nonDecreasing = True
#     nonIncreasing = True
#     for i in range(1, len(array)):
#         if array[i] > array[i - 1]:
#             nonIncreasing = False
#         elif array[i] < array[i-1]:
#             nonDecreasing = False
#     return nonDecreasing or nonIncreasing

# <------------ Approach 2 ------------------->

# Time Comlexity = O(n) | Space Complexity = O(1)

def isMonotonic(array):
    direction = ''
    if array[1] > array[0]:
        direction = 'INCREASING'
    elif array[1] > array[0]:
        direction = 'DECREASING'
    for i in range(2, len(array) - 2):
        if array[i] > array[i-1] and direction == '':
            direction = 'INCREASING'
        elif array[i] < array[i-1] and direction == '':
            direction = 'DECREASING'
        elif array[i] > array[i-1] and direction == 'DECREASING':
            return False
        elif array[i] < array[i - 1] and direction == 'INCREASING':
            return False
    return True