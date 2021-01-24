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
