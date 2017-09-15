class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0] * (len(prices) + 2)
        dp[-1] = 0
        for i in xrange(len(prices) - 2, -1, -1):
            dp[i] = dp[i + 1]
            for j in xrange(i + 1, len(prices)):
                dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2])
        return dp[0]
