# def min_abs_sum(A):
#     lenOfA = len(A)
#     M = 0
#     for i in range(lenOfA):
#         A[i] = abs(A[i])
#         M = max(A[i], M)
#     S = sum(A)
#     dp = [0 for _ in range(S+1)]
#     dp[0] = 1
#     for i in range(lenOfA):
#         print('inner for loop')
#         for j in range(S, -1, -1):
#             if (dp[j] == 1) and (j + A[i] <= S):
                
#                 dp[j + A[i]] = 1
#                 print(dp)
#     result = S
#     print(dp)
#     print(result)
#     for i in range(S // 2 + 1):
#         if dp[i] == 1:
#             result = min(result, S - 2 * i)
#     print(result)
#     return result


def min_abs_sum(A):
    lenOfA = len(A)
    M = 0
    for i in range(lenOfA):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(lenOfA):
        count[A[i]] += 1
    dp = [-1 for _ in range(S+1)]
    dp[0] = 0
    for i in range(1, M + 1):
        if count[i] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[i]
                elif (j >= i and dp[j - i] > 0):
                    dp[j] = dp[j - i] - 1                    
    result = S
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    print(result)
    return result

min_abs_sum([1,5,2,-2])