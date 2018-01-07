class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in xrange(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        
        return min(dp[-1], dp[-2])
