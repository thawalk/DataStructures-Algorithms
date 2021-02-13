# Time complexity =log10(n) | Space Complexity = O(log(n)), where n is the number that is to be reversed, because there is roughly log10(n) digits in n

def reverse(self, x):
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        last_digit = x % 10
        rev = int(rev * 10 + last_digit)
        x = int(x / 10)
    rev *= sign
    
    if (-2**31 <= rev < 2**31) == False:
        return 0
    
    return rev