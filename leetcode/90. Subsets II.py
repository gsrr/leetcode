import itertools

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = {}
        for i in xrange(len(nums) + 1):
            it = itertools.combinations(nums, i)
            for line in it:
                ret[line] = True
        return [ list(x) for x in ret.keys()]
        
