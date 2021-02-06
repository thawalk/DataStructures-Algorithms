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



