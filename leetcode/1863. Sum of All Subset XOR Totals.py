
total = 0

def ans(nums, i, val):
    global total
    if len(nums) == i:
        total += val
        return
    ans(nums, i + 1, val)
    ans(nums, i + 1, val^nums[i])
    

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global total
        total = 0
        ans(nums, 0, 0)
        return total
