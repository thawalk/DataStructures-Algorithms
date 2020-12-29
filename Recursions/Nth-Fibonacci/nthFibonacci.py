# Time Complexity = O(2^n), recursion will form a tree | Space Complexity = O(n), n frames on the call stack

# def getNthFib(n):
#     if n == 1: return 0
#     elif n == 2: return 1
#     return getNthFib(n - 1) + getNthFib(n - 2)

# Time Complexity = O(n), since there is no need to calculate prev calculated values | Space Complexity = O(n), to store the memo map

# def getNthFib(n, memo = {1:0, 2:1}):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = getNthFib(n - 1, memo) + getNthFib(n - 2, memo)
#         return memo[n]

# Time Complexity = O(n), single pass to get to the nth fibo number | Space Complexity = O(1), we don't store any other values other than the array

def getNthFib(n):
    # start from 3, because 0 and 1 is in the default
    counter = 3
    array = [0,1]
    while counter <= n:
        result = array[0] + array[1]
        array[0] = array[1]
        array[1] = result
        counter += 1
    return array[1] if n > 1 else array[0]





