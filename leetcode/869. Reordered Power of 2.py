import collections

def ans(n):
    if n == 1:
        return True
    
    
    bdic = []
    for i in xrange(40):
        ns = str(pow(2, i))
        bdic.append(collections.Counter(ns))
    #print bdic
    
    cn = collections.Counter(str(n))
    for i in xrange(len(bdic)):
        if bdic[i] == cn:
            return True
    return False

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return ans(N)
        
