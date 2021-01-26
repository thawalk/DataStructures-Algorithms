# <--------- Approach 1 brute-force ----------->
# Time Complexity = O(n^2) | Space Complexity = O(1)

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i == j:
                continue
            runningProduct *= array[j]
        products[i] = runningProduct
    return products

    
