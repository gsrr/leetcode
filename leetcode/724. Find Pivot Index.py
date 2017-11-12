def ans_3(nums):
    '''
    1. Create a summation array
    
    Time Complexity : O(n)
    Space Comlexity : O(n)
    Result : Accept
    '''
    n = len(nums)
    sarr = [0] * (n + 1)
    for i in xrange(n):
        sarr[i + 1] = sarr[i] + nums[i]
    
    for i in xrange(n):
        if sarr[i] == sarr[n] - sarr[i + 1]:
            return i
    return -1

def ans_2(nums):
    '''
    Time Complexity : O(n)
    Result : Accept
    '''
    s2 = sum(nums)
    s1 = 0
    for i in xrange(len(nums)):
        s2 -= nums[i]
        if s1 == s2:
            return i
        s1 += nums[i]
    return -1

def ans_1(nums):
    '''
    Time Complexity : O(n^2)
    Result : Time Limit Exceeded
    '''
    for i in xrange(len(nums)):
        larr = nums[0:i]
        rarr = nums[i + 1:]
        s1 = sum(larr)
        s2 = sum(rarr)
        if s1 == s2:
            return i
    return -1

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ans_3(nums)
