import itertools


def ans3(nums):
    nums.sort()
    ret = {}
    for i in xrange(len(nums) + 1):
        it = itertools.combinations(nums, i)
        for line in it:
            ret[line] = True
    return [ list(x) for x in ret.keys()]

import copy

def ans1(nums):
    nums.sort()
    ret = [[]]
    hist = {}
    for i in xrange(len(nums)):
        elems = copy.deepcopy(ret) # slowly
        for e in elems:
            e.append(nums[i])
            if hist.has_key(tuple(e)) == False:
                ret.append(list(e))
                hist[tuple(e)] = True
    return ret

def ans2(nums):
    '''
    Remove copy method
    '''
    nums.sort()
    ret = [[]]
    hist = {}
    for i in xrange(len(nums)):
        n = len(ret)
        for j in xrange(n):
            e = list(ret[j])
            e.append(nums[i])
            if hist.has_key(tuple(e)) == False:
                ret.append(e)
                hist[tuple(e)] = True
    return ret

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return ans2(nums)    
