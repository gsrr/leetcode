def ans(arr):
    return [ list(x) for x in zip(*arr) ]

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return ans(A)
