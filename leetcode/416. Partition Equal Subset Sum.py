def part_util(arr, sval, tval):
    if sval == tval:
        return True
    
    if sval > tval:
        return False
    
    for i in xrange(len(arr)):
        sval += arr[i]
        ret = part_util(arr[i + 1:], sval, tval)
        if ret == True:
            return True
        sval -= arr[i]
    return False
    
def ans1(arr):
    '''
    A simple method by recursive walking.
    Result : Time Limit Exceeded
    Time complexity : O(2^n) --> number of lookup
    Space complexity : stack of function call --> O(n)
    '''
    summ = sum(arr)
    if summ % 2 != 0:
        return False
    tval = summ / 2
    for i in xrange(len(arr)):
        sval = arr[i]
        ret = part_util(arr[i + 1:], sval, tval)
        if ret == True:
            return True
        sval -= arr[i]
    return False

def ans2(arr):
    '''
    Dynamic programming : The recursive stage solution can be solved by DP.
    Result : Accept
    Time complexity : O(n * tval)
    Space complexity : O(tval)
    '''
    summ = sum(arr)
    if summ % 2 != 0:
        return False
    
    tval = summ / 2
    dp = {}
    for i in xrange(len(arr)):
        for key in dp.keys():
            dp[key + arr[i]] = True
        dp[arr[i]] = True
    if dp.has_key(tval):
        return True
    return False

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return ans2(nums)
