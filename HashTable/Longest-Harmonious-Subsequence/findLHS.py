def findLHS(nums):
    nums.sort()
    prev_count = 1
    res = 0
    for i in range(len(nums)):
        count = 1
        if i > 0 and (nums[i] - nums[i - 1] == 1):
            while i < (len(nums) - 1) and nums[i] == nums[i+1]:
                count += 1
                i+=1
            res = max(res, count + prev_count)
            prev_count = count
        else:
            while i < (len(nums) - 1) and nums[i] == nums[i+1]:
                count += 1
                i+=1
            prev_count = count
    return res



import itertools
from collections import deque

def findMinDistance(w, h, n):
    array = []
    for i in range(h):
        for j in range(w):
            array.append((i,j,0))
    result = float("inf")
    for points in itertools.combinations(array, n):
        q = deque()
        visited = set()
        for m, n, dist in points:
            q.append((m,n, dist))
            visited.add((m,n))
        distAns = 0
        distArr = []
        while q:
            i, j, dist = q.popleft()
            distAns = max(dist, distAns)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0<=x<h and 0<=y<w and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        result = min(distAns, result)
    return result