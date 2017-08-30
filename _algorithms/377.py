hist = {}

def ans1(nums, target):
    if target < 0 :
        return 0
    if hist.get(target) != None:
        return hist.get(target)
    
    if target == 0:
        return 1
    cnt = 0
    for i in xrange(len(nums)):
        cnt += ans1(nums, target - nums[i])
    hist[target] = cnt
    return cnt

def ans2(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in xrange(target + 1):
        for j in  xrange(len(nums)):
            if i + nums[j] < len(dp):
                dp[i + nums[j]] += dp[i]
    return dp[target]

def ans3(nums, target):
    dp = [0] * (target + 1)
    dp[target] = 1
    for i in xrange(target, -1, -1):
        for j in xrange(len(nums)):
            if i - nums[j] >= 0:
                dp[i - nums[j]] += dp[i]
    return dp[0]

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        global hist
        hist = {}
        if len(nums) == 0:
            return 0
        #return ans1(nums, target)
        #return ans2(nums, target)
        return ans3(nums, target)
