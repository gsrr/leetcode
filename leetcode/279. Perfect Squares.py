import bisect
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqs = []
        i = 1
        while i * i <= n:
            sqs.append(i * i)
            i += 1
        print sqs
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in xrange(1, n + 1):
            idx = bisect.bisect_right(sqs, i)
            min_val = 999
            for j in xrange(idx - 1, -1, -1):
                min_val = min(min_val, 1 + dp[i - sqs[j]])
            dp[i] = min_val
        return dp[n]
