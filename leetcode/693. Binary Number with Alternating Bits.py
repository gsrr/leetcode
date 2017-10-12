class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bn = bin(n)[2:]
        for i in xrange(1, len(bn)):
            if bn[i] != bn[i - 1]:
                continue
            else:
                return False
        return True
