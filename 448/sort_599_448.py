class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        cur = 1
        nums.sort()
        start = 0
        while cur <= len(nums):
            find = False
            for i in xrange(start, len(nums)):
                if nums[i] == cur:
                    find = True
                    start = i
                    break
                elif cur < nums[i]:
                    start = i
                    break
            if find == False:
                result.append(cur)
            cur += 1
        return result