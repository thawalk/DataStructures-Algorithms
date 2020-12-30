# <----------- Using pointers, this is the most optimal solution ----------->  

# Time Complexity = O(n) | Space Complexity = O(1)

# def isPalindrome(string):
#     leftP = 0
#     rightP = len(string) - 1
#     while leftP < rightP:
#         if string[leftP] != string[rightP]:
#             return False
#         leftP += 1
#         rightP -= 1
#     return True

# <----------- Using a string to store the reverse -----------> 

# Time Complexity = O(n^2), because string in python is immutable, so need to keep copying it over | Space Complexity = O(n) 

# def isPalindrome(string):
#     compare = ""
#     for i in range(1, len(string) + 1):
#         compare += string[-i]
#     return compare == string

# <----------- Using a list to store the reverse ----------->

# Time Complexity = O(n) | Space Complexity = O(n) 

# def isPalindrome(string):
#     compare = []
#     for i in range(1, len(string) + 1):
#         compare.append(string[-i])
#     return "".join(compare) == string

# <----------- Recursion ----------->

# Time Complexity = O(n) | Space Complexity = O(n) 

def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    else:
        return string[i] == string[j] and isPalindrome(string, i + 1)
