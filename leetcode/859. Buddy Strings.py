import collections

def ans(A, B):
    pos = []
    for i in xrange(len(A)):
        if A[i] != B[i]:
            pos.append(i)
    if len(pos) != 2 and len(pos) != 0:
        return False
    if len(pos) == 2:
        if A[pos[0]] == B[pos[1]] and A[pos[1]] == B[pos[0]]:
            return True
    if len(pos) == 0:
        ct = collections.Counter(A)
        for key in ct.keys():
            if ct[key] > 1:
                return True
    return False

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return ans(A, B)
