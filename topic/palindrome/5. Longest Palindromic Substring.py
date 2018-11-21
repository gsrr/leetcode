def ans(s):
    dp = [ [0] * len(s) for _ in xrange(len(s)) ]
    
    gcnt = 0
    gs = 0
    ge = 0
    for i in xrange(len(dp)):
        for j in xrange(len(dp)):
            if j + i >= len(dp):
                break
            if s[j] != s[j + i]:
                dp[j][j + i] = False
            else:
                if j + 1 >= j + i - 1:
                    dp[j][j + i] = True
                else:
                    #print j, j + i
                    dp[j][j + i] = dp[j + 1][j + i - 1]
                if dp[j][j + i] == True:
                    if i + 1 > gcnt:
                        gcnt = i + 1
                        gs = j
                        ge = j + i + 1
                        
    return s[gs : ge]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ans(s)
        
