def ans1(L, R):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    cnt = 0
    for i in xrange(L, R + 1):
        ones = bin(i).count("1")
        if ones in primes:
            cnt += 1
    return cnt

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return ans1(L, R)
        
        
