# 42 ms, 82%
class Solution:
    def twoSum(self, nums, target):
        history = {}
        for i in xrange(len(nums)):
            x = nums[i]
            if target - x in history:
                return (history[target - x], i)
            history[x] = i