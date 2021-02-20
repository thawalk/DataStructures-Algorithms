# Time Complexity = O(n) | Space Complexity = O(1)

def numberOfArithmeticSlices(self, A):
    dp = 0
    res = 0
    for i in range(2, len(A)):
        if A[i] - A[i-1] == A[i - 1] - A[i-2]:
            dp = 1 + dp
            res += dp
        else:
            dp = 0
    return res