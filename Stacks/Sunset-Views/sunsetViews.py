# <----------- Approach 1 ------------>

# Time Complexity = O(n) | Space Complexity = O(n) 

# def sunsetViews(buildings, direction):
#         runningMax = 0
#         answer = []
#         if direction == "EAST":
#             startIdx = len(buildings) - 1
#             endIdx = -1
#             step = -1
#         else:
#             startIdx = 0
#             endIdx = len(buildings)
#             step = 1
#         for i in range(startIdx, endIdx, step):
#             if buildings[i] > runningMax:
#                 answer.append(i)
#                 runningMax = buildings[i]
#         if direction == "EAST":
#             return answer[::-1]
#         return answer

# <----------- Approach 2 using stack------------>

# Time Complexity = O(n) | Space Complexity = O(n) 

def sunsetViews(buildings, direction):
    stack = []
    if direction == "WEST":
        startIdx = len(buildings) - 1
        endIdx = -1
        step = -1
    else:
        startIdx = 0
        endIdx = len(buildings)
        step = 1
    for i in range(startIdx, endIdx, step):
        if not len(stack):
            stack.append(i)
        else:
            for j in range(len(stack) - 1, -1, -1):
                if buildings[i] >= buildings[stack[j]]:
                    stack.pop()
                else:
                    break
            stack.append(i)
    if direction == "WEST":
        return stack[::-1]
    return stack