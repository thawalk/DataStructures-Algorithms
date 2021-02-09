class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        p1 = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += p1
                if lin == 0 or lin == numRows - 1:
                    p1 *= -1
        outputStr = ''
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr