def getset(n):
    tmp = []
    while n != 0:
        r = n % 10
        n = n / 10
        tmp.append(r)
    return set(tmp)

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nset = set([3,4,7])
        gset = set([2,5,6,9])
        cnt = 0
        for i in xrange(1, N + 1):
            seti = getset(i)
            if len(seti & nset) != 0:
                continue
            if len(seti & gset) != 0:
                cnt += 1
        return cnt
