# 6000ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i,j]
