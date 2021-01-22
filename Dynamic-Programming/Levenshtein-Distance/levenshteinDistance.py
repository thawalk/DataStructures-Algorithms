# <----------------- Approach 1 ------------------->

# Time Complexity = O(nm) | Space Complexity = O(nm)

# def levenshteinDistance(str1, str2):
#     edits = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
#     for i in range(1, len(str1) + 1):
#         edits[i][0] = edits[i - 1][0] + 1
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 edits[i][j] = edits[i - 1][j - 1]
#             else:
#                 edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])
#     return edits[-1][-1]

# <-------------- Approach 2 using only 2 rows, thus lesser space required ---------------------->

# Time Comlexity = O(nm) | Space Complexity = O(min(n, m))

def levenshteinDistance(str1, str2):
    # we want the columns to be smaller, so we can store less overall, since we are only storing 2 rows at a time
    columns = str1 if len(str1) < len(str2) else str2
    rows = str1 if len(str1) >= len(str2) else str2
    oddEdits = [x for x in range(len(columns) + 1)]
    evenEdits = [None for x in range(len(columns) + 1)]
    for i in range(1,len(rows) + 1):
        if i % 2 == 1:
            currentEdit = evenEdits
            prevEdit = oddEdits
        else:
            currentEdit = oddEdits
            prevEdit = evenEdits
        currentEdit[0] = i
        for j in range(1, len(columns) + 1):
            if columns[j - 1] == rows[i - 1]:
                currentEdit[j] = prevEdit[j - 1]
            else:
                currentEdit[j] = 1 + min(currentEdit[j-1], prevEdit[j-1], prevEdit[j])
    return evenEdits[-1] if len(rows) % 2 == 0 else oddEdits[-1]
