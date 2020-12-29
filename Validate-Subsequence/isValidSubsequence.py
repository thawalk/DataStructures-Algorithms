# Time Complexity = O(n) | Space Complexity = O(1)

# def isValidSubsequence(array, sequence):
#     arrayP = 0
#     seqP = 0
#     while arrayP < len(array) and seqP < len(sequence):
#         if array[arrayP] == sequence[seqP]:
#             seqP += 1
#         arrayP += 1
#     return seqP == len(sequence)

#  <---------------- Less Iterations ---------------->
# Time Complexity = O(n) | Space Complexity = O(1)
def isValidSubsequence(array, sequence):
    seqP = 0
    for value in array:
        if seqP == len(sequence):
            break
        if value == sequence[seqP]:
            seqP += 1
    return seqP == len(sequence)