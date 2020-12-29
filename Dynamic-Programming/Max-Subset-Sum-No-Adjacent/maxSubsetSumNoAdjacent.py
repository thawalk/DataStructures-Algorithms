# Time Complexity = O(N) | Space Complexity = O(N), to create the list maxSums

# def maxSubsetSumNoAdjacent(array):
#     if len(array) == 0: return 0
#     if len(array) == 1: return array[0]
#     maxSums = [array[0], max(array[0], array[1])]
#     idx = 2
#     while idx < len(array):
#         sumWithEarlier = maxSums[idx - 2] + array[idx]
#         prev = maxSums[idx - 1]
#         maxSums.append(max(sumWithEarlier, prev))
#         idx += 1
#     return maxSums[-1]

# Time Complexity = O(N) | Space Complexity = O(1), because no list is needed

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0: return 0
    if len(array) == 1: return array[0]
    idx = 2
    second = array[0]
    first = max(array[1], array[0])
    while idx < len(array):
        sumWithEarlier = second + array[idx]
        second = first
        first = max(sumWithEarlier, first)
        idx += 1
    return first

