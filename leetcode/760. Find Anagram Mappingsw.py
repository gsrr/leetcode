class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        P = [0] * len(A)
        B_dic = {}
        for i in xrange(len(B)):
            B_dic[B[i]] = i
        
        for i in xrange(len(A)):
            P[i] = B_dic[A[i]]
        return P
