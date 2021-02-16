def letterCasePermutation(self, S):
    ans = [[]]
    
    for char in S:
        n = len(ans)
        if char.isalpha():
            for i in range(n):
                ans.append(ans[i][:])
                ans[i].append(char.lower())
                ans[n+i].append(char.upper())

        else:
            for i in range(n):
                ans[i].append(char)
                
    return map("".join, ans)