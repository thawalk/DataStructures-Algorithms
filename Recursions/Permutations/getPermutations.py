# <----------------- First Solution ------------------->

# Time Complexity = O(n!*n^2) | Space Complexity = O(n!*n)

# def getPermutations(array):
#     permutations = []
#     getPermutationsHelper(array, [], permutations)
#     return permutations

# def getPermutationsHelper(currentArray, currentPerm, permutations):
#     if not len(currentArray) and len(currentPerm):
#         permutations.append(currentPerm)
#     else:
#         for j in range(len(currentArray)):
#             newArray = currentArray[:j] + currentArray[j+1:]
#             newPerm = currentPerm + [currentArray[j]]
#             getPermutationsHelper(newArray, newPerm, permutations)

# <----------------- Second Solution ------------------->

# Time Complexity = O(n!*n) | Space Complexity = O(n!*n)

def getPermutations(array):
    permutations = []
    getPermutationsHelper(array, 0, permutations)
    return permutations 

def getPermutationsHelper(array, idx, permutations):
    if idx == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(idx, len(array)):
            swap(idx, j, array)
            getPermutationsHelper(array, idx + 1, permutations)
            swap(idx, j, array)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
