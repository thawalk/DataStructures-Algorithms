# Time Complexity = O(nlogn) | Space Complexity = O(1), is language dependent

# def isAnagram(self, s, t):
#     return len(s) == len(t) and sorted(s) == sorted(t)

# Time Complexity = O(n) | Space Complexity = O(1), is language dependent

def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        table = [0] * 26
        
        for char in s:
            table[ord(char) - ord('a')] += 1
            
        for char in t:
            table[ord(char) - ord('a')] -= 1
            
        for value in table:
            if value != 0:
                return False
        return True
