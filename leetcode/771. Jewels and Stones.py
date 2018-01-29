import collections

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jdic = collections.Counter(J)
        sdic = collections.Counter(S)
        cnt = 0
        for key in jdic.keys():
            cnt += sdic.get(key, 0)
        return cnt
    
        
