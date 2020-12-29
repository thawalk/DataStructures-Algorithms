# Time Complexity = O(nd), where d is the number of denoms, n is the input integer 
# Space Complexity = O(n), to main the list of ways

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]