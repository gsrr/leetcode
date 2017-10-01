class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sa = A
        cnt = 2
        while len(sa) <= len(B):
            sa = A * cnt
            cnt += 1
        sa = A * cnt
        
        if B in sa:
            return sa.index(B)
        else:
            return -1 
