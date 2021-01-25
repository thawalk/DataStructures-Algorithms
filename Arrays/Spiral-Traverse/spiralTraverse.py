# <------ Approach 1 Iterative ------->

# Time Complexity = O(n) | Space Complecity = O(n) 

# def spiralTraverse(array):
#     result = []
#     startColumn, endColumn = 0, len(array[0]) - 1
#     startRow, endRow = 0, len(array) - 1
    
#     while startColumn <= endColumn and startRow <= endRow:
#         for col in range(startColumn, endColumn + 1):
#             result.append(array[startRow][col])
        
#         for row in range(startRow + 1, endRow + 1):
#             result.append(array[row][endColumn])

#         for col in reversed(range(startColumn, endColumn)):
#             if startRow == endRow:
#                 break
#             result.append(array[endRow][col])

#         for row in reversed(range(startRow + 1, endRow)):
#             if startColumn == endColumn:
#                 break
#             result.append(array[row][startColumn])

#         startColumn += 1
#         endColumn -= 1
#         startRow += 1
#         endRow -= 1

#     return result

# <------ Approach 2 Recursive ------->

# Time Complexity = O(n) | Space Complecity = O(n) 

def spiralTraverse(array):
    result = []
    startColumn, endColumn = 0, len(array[0]) - 1
    startRow, endRow = 0, len(array) - 1
    spiralTraverseHelper(array, startColumn, endColumn, startRow, endRow, result)
    return result

def spiralTraverseHelper(array, startColumn, endColumn, startRow, endRow, result):

    if startColumn > endColumn and startRow > endRow:
        return 
    
    for col in range(startColumn, endColumn + 1):
        result.append(array[startRow][col])
    
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endColumn])

    for col in reversed(range(startColumn, endColumn)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        if startColumn == endColumn:
            break
        result.append(array[row][startColumn])
    
    spiralTraverseHelper(array, startColumn + 1, endColumn - 1, startRow + 1, endRow - 1, result)