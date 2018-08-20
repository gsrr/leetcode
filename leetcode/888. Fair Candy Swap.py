import collections

def ans(A, B):
    cb = collections.Counter(B)
    sa = sum(A)
    sb = sum(B)
    mid = (sa + sb) / 2
    for i in xrange(len(A)):
        b = mid - (sa - A[i])
        if cb.has_key(b):
            return [A[i], b]
        

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        return ans(A, B)
        
