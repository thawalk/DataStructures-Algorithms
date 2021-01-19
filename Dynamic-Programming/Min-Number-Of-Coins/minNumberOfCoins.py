# Time Complexity = O(nd), where n is the target number and d is the number of denoms | Space Complexity = O(n) 

def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf")  for i in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for coin in range(len(numOfCoins)):
            if denom <= coin:
                remainderCoins = numOfCoins[coin - denom]
                numOfCoins[coin] = min(numOfCoins[coin], remainderCoins + 1)
    return numOfCoins[-1] if numOfCoins[-1] != float("inf") else -1

    
                