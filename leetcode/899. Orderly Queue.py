def ans(ss, k):
    arr = list(ss)
    if k > 1:
        arr.sort()
        return "".join(arr)
    
    ss2 = ss * 2
    arrs = []
    for i in xrange(len(ss)):
        arrs.append(ss2[i: i + len(ss)])
    arrs.sort()
    return arrs[0]
    
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        return ans(S, K)
        
