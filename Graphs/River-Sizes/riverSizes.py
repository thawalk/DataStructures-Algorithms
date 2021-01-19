# Time Complexity = O(wh) | Space Complexity = O(wh) 

def riverSizes(matrix):
    answer = []
    visited = [[False for value in elem]for elem in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, matrix, visited, answer)
    return answer

def traverseNodes(i, j, matrix, visited, answer):
    currentLength = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentLength += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentLength > 0:
        answer.append(currentLength)

def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix) - 1 and not visited[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    return unvisitedNeighbours
    

