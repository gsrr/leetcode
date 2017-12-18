import collections

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cnums = collections.Counter(nums)
        dp = [0] * 10001
        if cnums.has_key(1):
            dp[1] = cnums[1]
        for i in xrange(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + cnums.get(i, 0) * i)

        return dp[-1]
    
