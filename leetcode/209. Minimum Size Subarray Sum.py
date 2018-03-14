          
def ans2(s, arr):
    ret = len(arr) + 1
    i, j = 0, 0
    ts = 0
    while j < len(arr):
        ts += arr[j]
        while ts >= s:
            ret = min(ret, j - i + 1)
            ts -= arr[i]
            i += 1
        j += 1        
    if ret == len(arr) + 1:
        return 0
    return ret
    
def ans1(s, arr):
    '''
    Result :  Time Limit Exceeded
    Time Complexity : O(n^2)
    '''
    ret = len(arr) + 1
    for i in xrange(len(arr)):
        ts = 0
        for j in xrange(i, len(arr)):
            ts += arr[j]
            if ts >= s:
                ret = min(j - i + 1, ret)
                break
    if ret == len(arr) + 1:
        return 0
    return ret

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        return ans2(s, nums)
        
