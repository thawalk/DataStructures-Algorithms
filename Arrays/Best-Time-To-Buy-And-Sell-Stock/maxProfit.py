# <----- Approach 1 Single Pass ----->

# Time Complexity = O(n) | Space Complexity = O(1)

def maxProfit(prices):
    minPrice = float("inf")
    maxProfit = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
        elif (price - minPrice) > maxProfit:
            maxProfit = price - minPrice
    print(maxProfit)
    return maxProfit

# <----- Approach 2 Brute Force ----->

# Time Complexity = O(n^2) | Space Complexity = O(1)

# def maxProfit(prices):
#     maxProfit = 0
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             if prices[j] - prices[i] > maxProfit:
#                 maxProfit = prices[j] - prices[i]
#     print(maxProfit)
#     return maxProfit



maxProfit([7,1,5,3,6,4])