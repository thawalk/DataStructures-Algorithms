# Time Complexity = O(n) | Space Complexity = O(n)

def shortestToChar(s, c):
    prev = float("-inf")
    answer = []
    for i, x in enumerate(s):
        if x == c: prev = i 
        answer.append(i - prev)
    
    prev = float("inf")
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c: prev = i 
        answer[i] = min(answer[i], prev - i)
        
    return answer