class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        nums.sort()
        cur = 1
        i = 0
        while i < len(nums):
            if nums[i] == cur:
                cur += 1
                i += 1
            elif nums[i] > cur:
                result.append(cur)
                cur += 1
            elif nums[i] < cur:
                i += 1
        
        while cur <= len(nums):
            result.append(cur)
            cur += 1
        return result