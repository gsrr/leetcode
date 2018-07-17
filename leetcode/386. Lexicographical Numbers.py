class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [str(x) for x in xrange(1, n + 1)]
        arr.sort()
        ret = [int(x) for x in arr]
        return ret
