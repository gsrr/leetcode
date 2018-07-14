def ans(n, back):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        if back == 1:
            return 2 * (ans(n/2, 1 - back) - 1) + 1
        else:
            return 2 * ans(n / 2, 1 - back)
    else:
        return 2 * ans(n / 2, 1 - back)
        

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        return 2 * ans(n/2, 1)
