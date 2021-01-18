# <------------ Approach 1 Iterative -------------->

# Time Complexity = O(n * 2^n)| Space Complexity = O(n * 2^n) 

# def powerset(array):
#     answer = [[]]
#     for elem in array:
#         for i in range(len(answer)):
#             newSubArray = answer[i]
#             answer.append(newSubArray + [elem])
#     return answer

# <------------ Approach 2 Recursive -------------->

# Time Complexity = O(n * 2^n)| Space Complexity = O(n * 2^n) 

def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    elem = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [elem])
    return subsets
