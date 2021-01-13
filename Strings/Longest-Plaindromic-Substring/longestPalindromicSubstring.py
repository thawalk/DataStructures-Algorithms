# Time Complexity = O(n^3) | Space Complexity = O(n)

# run through all the possible substrings
# def longestPalindromicSubstring(string):
#     longestPalindrome = ""
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             substring = string[i: j + 1]
#             if len(substring) > len(longestPalindrome) and isPalindrome(substring):
#                 longestPalindrome = substring
#     return longestPalindrome

# def isPalindrome(string):
#     leftIdx = 0
#     rightIdx = len(string) - 1
#     while leftIdx < rightIdx:
#         if string[leftIdx] != string[rightIdx]:
#             return False
#         leftIdx += 1
#         rightIdx -= 1
#     return True

# Time Complexity = O(n^2) | Space Complexity = O(n)

# maintain an array to store the indexes of the longest palindrome

def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for i in range(1, len(string)):
        oddPalindrome = getLongestPalindromeFrom(string, i-1, i+1)
        evenPalindrome = getLongestPalindromeFrom(string, i - 1, i)
        longest =  max(oddPalindrome, evenPalindrome, key= lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longest, key= lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]
        

