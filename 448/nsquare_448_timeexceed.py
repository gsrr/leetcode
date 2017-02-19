class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        cur = 1
        while cur <= len(nums):
            find = False
            for i in xrange(0, len(nums)):
                if nums[i] == cur:
                    find = True
                    break
            if find == False:
                result.append(cur)
            cur += 1
        return result