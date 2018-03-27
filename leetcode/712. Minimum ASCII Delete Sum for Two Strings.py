def ans1(s1, s2):
    dp = [[(0, 0)] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
    for i in xrange(1, len(dp)):
        for j in xrange(1, len(dp[i])):
            num, summ = dp[i - 1][j - 1]
            if s1[i - 1] == s2[j - 1]:
                num += 1
                summ += ord(s1[i - 1])
                dp[i][j] = (num, summ)
            else:
                n1, summ1 = dp[i - 1][j]
                n2, summ2 = dp[i][j - 1]
                if summ1 > summ2:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    summ = 0
    for c in s1:
        summ += ord(c)
    for c in s2:
        summ += ord(c)
    return summ - (dp[-1][-1][1] * 2)

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        return ans1(s1, s2)
        
