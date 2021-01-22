# Time Complexity = O(n) | Space Complexity = O(1)

def decodeWays(string):
    if string[0] == '0':
        return 0
    
    # save just the last 2 dp values
    twoBack = 1
    oneBack = 1
    idx = 1

    while idx < len(string):
        current = 0
        if string[idx] != '0':
            current += oneBack
        
        twoDigit = int(string[idx - 1: idx + 1])
        if twoDigit >= 10 and twoDigit <= 26:
            current += twoBack

        twoBack = oneBack
        oneBack = current
        idx += 1
        
    print(oneBack)
    return oneBack

decodeWays('2125')
# Answer = 5