# Time Complexity = O(nlogn) | Space Complexity = O(1), is language dependent

def isAnagram(self, s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)

