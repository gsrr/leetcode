def ans(A):
    la = [0] * len(A)
    ra = [0] * len(A)
    for i in xrange(1, len(A)):
        if A[i] > A[i - 1]:
            la[i] = la[i - 1] + 1
        else:
            la[i] = 0
    
    for i in xrange(len(A) - 2, -1, -1):
        if A[i] > A[i + 1]:
            ra[i] = ra[i + 1] + 1
        else:
            ra[i] = 0
    
    mval = 0
    for i in xrange(len(A)):
        if la[i] != 0 and ra[i] != 0:
            mval = max(mval, la[i] + ra[i])
    if mval < 2:
        return 0
    return mval + 1
    
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
