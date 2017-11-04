def ans_1(k, prices):
    '''
    Inspired from ans_5, 
    1. create a array with element : [hold, release]
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    Result : Accept
    '''
    arr = [[-0x80000000, 0] for _ in xrange(k)]
    arr.append([0, 0])
    for p in prices:
        for i in xrange(k):
            arr[i][1] = max(arr[i][1], arr[i][0] + p)
            arr[i][0] = max(arr[i][0], arr[i + 1][1] - p)
    return arr[0][1]

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        cnt = 0
        s = 0
        for i in xrange(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                cnt += 1
                s += (prices[i] - prices[i - 1])
        if k >= cnt:
            return s
        return ans_1(k, prices)
