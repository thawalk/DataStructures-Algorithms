# <---------------- Approach 1 -------------------->
# Time Complexity = O(v+e) | Space Complexity = O(v)

def cycleInGraph(edges):
    numOfNodes = len(edges)
    visited = [False for _ in range(numOfNodes)]
    stack = [False for _ in range(numOfNodes)]

    for node in range(len(edges)):
        if visited[node]:
            continue

        containsCycle = isNodeCycle(node, visited, stack, edges)
        if containsCycle:
            return True
    return False

def isNodeCycle(node, visited, stack, edges):
    visited[node] = True
    stack[node] = True
    neighbours = edges[node]

    for neighbour in neighbours:
        if not visited[neighbour]:
            containsCycle = isNodeCycle(neighbour, visited, stack, edges)
            if containsCycle:
                return True
        elif stack[neighbour]:
            return True

    stack[node] = False
    return False

# <---------------- Approach 2 -------------------->
# Time Complexity = O(v+e) | Space Complexity = O(v)

WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph(edges):
    numOfNodes = len(edges)
    colors = [WHITE for _ in range(numOfNodes)]

    for node in range(numOfNodes):
        if colors[node] != WHITE:
            continue

        containsCycle = traverseAndColorNodes(node, colors, edges)
        if containsCycle:
            return True
    return False

def traverseAndColorNodes(node, colors, edges):
    colors[node] = GREY
    neighbours = edges[node]

    for neighbour in neighbours:
        if colors[neighbour] == WHITE:
            containsCycle = traverseAndColorNodes(neighbour, colors, edges)
            if containsCycle:
                return True
        elif colors[neighbour] == GREY:
            return True

    colors[node] = BLACK
    return False