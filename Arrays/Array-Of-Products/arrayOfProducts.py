# <--------- Approach 1 brute-force ----------->
# Time Complexity = O(n^2) | Space Complexity = O(1)

# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]
#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i == j:
#                 continue
#             runningProduct *= array[j]
#         products[i] = runningProduct
#     return products


# <--------- Approach 2 using supplementary arrays ----------->
# Time Complexity = O(n) | Space Complexity = O(n)

# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]
#     leftProducts = [1 for _ in range(len(array))]
#     rightProducts = [1 for _ in range(len(array))]
#     leftProduct, rightProduct = 1, 1

#     for i in range(1,len(array)):
#         leftProduct *= array[i-1]
#         leftProducts[i] = leftProduct

#     for i in reversed(range(len(array)-1)):
#         rightProduct *= array[i+1]
#         rightProducts[i] = rightProduct

#     for i in range(len(array)):
#         products[i] = leftProducts[i] * rightProducts[i]
    
#     return products

# <--------- Approach 3 without using supplementary arrays ----------->
# Time Complexity = O(n) | Space Complexity = O(n)

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProduct, rightProduct = 1, 1

    for i in range(1,len(array)):
        leftProduct *= array[i-1]
        products[i] *= leftProduct

    for i in reversed(range(len(array)-1)):
        rightProduct *= array[i+1]
        products[i] *= rightProduct

    return products
    

