def ans(word1, word2):
    dp = [ [0] * (len(word1) + 1) for _ in xrange(len(word2) + 1) ]
    #print dp
    for i in xrange(len(word2)):
        for j in xrange(len(word1)):
            if word2[i] == word1[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    #print dp[-1][-1]
    return len(word1) + len(word2) - 2 * dp[-1][-1]
    
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return ans(word1, word2)
        
