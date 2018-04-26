import collections

def ans(A):
    A.sort()
    dic = collections.Counter(A)
    cnt = len(A)
    print A
    for i in xrange(len(A)):
        for j in xrange(len(A)):
            val = A[i] * A[j]
            if dic.has_key(val):
                cnt += (dic[A[i]] * dic[A[j]])
                dic[val] += (dic[A[i]] * dic[A[j]])
    return cnt

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
        
