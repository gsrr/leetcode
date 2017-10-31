def ans_1(arr):
    '''
    1. Create a difference array.
    2. Sum of all positive value
    
    Time complexity : O(n)
    Result : Accept
    '''
    diffArr = [ arr[i] - arr[i - 1] for i in xrange(1, len(arr))]
    s = 0
    for i in xrange(len(diffArr)):
        if diffArr[i] > 0:
            s += diffArr[i]
    return s

def ans_2(arr):
    '''
    Without difference array
    
    Time complexity : O(n)
    Result : Accept
    '''
    s = 0 
    for i in xrange(1, len(arr)):
        s += max(0, arr[i] - arr[i - 1])
    return s

def ans_3(arr):
    '''
    Two variable for solving
    
    Time Complexity : O(n)
    Result : Accept
    '''
    if len(arr) == 0:
        return 0
    
    pt = 0
    i = 0
    j = 0
    while i < len(arr) and j < len(arr) - 1:
        if arr[j + 1] > arr[j]:
            j += 1
        else:
            pt += max(0, arr[j] - arr[i])
            j += 1
            i = j
    pt += max(0, arr[j] - arr[i])
    return pt

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return ans_3(prices)
