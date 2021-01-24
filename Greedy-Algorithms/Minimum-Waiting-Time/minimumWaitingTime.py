# Time Complexity = O(nlogn), to sort the array| Space Complexity = O(1)

def minimumWaitingTime(queries):
    queries.sort()
    total = 0
    for idx in range(len(queries)):
        queriesLeft = len(queries) - 1 - idx
        total += (queries[idx] * queriesLeft)
    return total