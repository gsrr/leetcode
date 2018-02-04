def ans(N, K):
    if K == 1:
        return 0
    ln = N - 1
    nums = pow(2, ln - 1)
    if K - nums <= 0:
        return ans(N - 1, K)
    else:
        return 1 - ans(N - 1, K - nums)

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return ans(N, K)
