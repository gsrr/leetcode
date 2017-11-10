def ans_3(prices):
    '''
    Dynamic Programming (from selling stock)
    
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    '''
    if len(prices) == 0:
        return 0
    dp = [0] * (len(prices) + 2)
    for i in xrange(len(prices) - 1, -1, -1):
        dp[i] = dp[i + 1]
        for j in xrange(i, len(prices)):
            dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2])
    print dp
    return dp[0]

def ans_2(prices):
    '''
    Dynamic Programming (from buying stock)
    
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    '''
    if len(prices) == 0:
        return 0
    dp = [0] * (len(prices) + 2)
    for i in xrange(1, len(prices)):
        di = i + 2
        dp[di] = dp[di - 1]
        for j in xrange(i, -1, -1):
            dj = j + 2
            dp[di] = max(dp[di], prices[i] - prices[j] + dp[dj - 2])
    
    return dp[-1]

def ans_1(prices):
    '''
    Dynamic Programming (from buying stock)
    
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    '''
    if len(prices) == 0:
        return 0
    dp = [0] * (len(prices) + 2)
    for i in xrange(1, len(prices)):
        dp[i] = dp[i - 1]
        for j in xrange(i, -1, -1):
            dp[i] = max(dp[i], prices[i] - prices[j] + dp[j - 2])
    
    return dp[-3]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return ans_3(prices)
        
