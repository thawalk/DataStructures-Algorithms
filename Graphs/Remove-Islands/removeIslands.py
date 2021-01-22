# <---------- Approach 1 ----------->
# Time Complexity = O(wh) | Space Complexity = O(wh)

# def removeIslands(matrix):
#     onesConnectedBorder = [[False for col in matrix[0]] for row in matrix]

#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             horizBorder = row == 0 or row == len(matrix) - 1
#             vertBorder = col == 0 or col == len(matrix[row]) - 1
#             if horizBorder or vertBorder:
#                 if matrix[row][col] == 1:
#                     findOnesConnectedToBorder(matrix, row, col, onesConnectedBorder)

#     for row in range(1, len(matrix) - 1):
#         for col in range(1, len(matrix[row]) - 1):
#             if onesConnectedBorder[row][col]:
#                 continue

#             matrix[row][col] = 0
#     return matrix

# def findOnesConnectedToBorder(matrix, row, col, onesConnectedBorder):
#     stack = [[row, col]]
#     while len(stack):
#         currentNode = stack.pop()
#         row, col = currentNode[0], currentNode[1]
#         if onesConnectedBorder[row][col]:
#             continue
#         onesConnectedBorder[row][col] = True
#         neighbours = getNeighbours(row, col, matrix)
#         for neighbour in neighbours:
#             row, col = neighbour[0], neighbour[1]
#             if matrix[row][col] != 1:
#                 continue
#             stack.append(neighbour)

# def getNeighbours(i, j, matrix):
#     neighbours = []

#     if i - 1 >= 0:
#         neighbours.append([i - 1, j])
#     if i + 1 < len(matrix):
#         neighbours.append([i + 1, j])
#     if j - 1>= 0:
#         neighbours.append([i, j - 1])
#     if j + 1 < len(matrix[i]):
#         neighbours.append([i, j + 1])
#     return  neighbours

# <---------- Approach 2 ----------->
# Time Complexity = O(wh) | Space Complexity = O(wh)

def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            horizBorder = row == 0 or row == len(matrix) - 1
            vertBorder = col == 0 or col == len(matrix[row]) - 1
            if horizBorder or vertBorder:
                if matrix[row][col] == 1:
                    findOnesConnectedToBorder(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
            elif matrix[row][col] == 2:
                matrix[row][col] = 1

    return matrix

def findOnesConnectedToBorder(matrix, row, col):
    stack = [[row, col]]
    while len(stack):
        currentNode = stack.pop()
        row, col = currentNode[0], currentNode[1]
        matrix[row][col] = 2
        neighbours = getNeighbours(row, col, matrix)
        for neighbour in neighbours:
            row, col = neighbour[0], neighbour[1]
            if matrix[row][col] != 1:
                continue
            stack.append(neighbour)

def getNeighbours(i, j, matrix):
    neighbours = []

    if i - 1 >= 0:
        neighbours.append([i - 1, j])
    if i + 1 < len(matrix):
        neighbours.append([i + 1, j])
    if j - 1>= 0:
        neighbours.append([i, j - 1])
    if j + 1 < len(matrix[i]):
        neighbours.append([i, j + 1])
    return  neighbours