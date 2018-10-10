
def ans(num):
    sn = str(num)
    s = 0
    e = len(sn)
    for i in xrange(len(sn)/2):
        if sn[i] != sn[e - 1 - i]:
            return False
    return True

def ans1(num):
    if num == 0:
        return True
    if num < 0:
        return False
    if num % 10 == 0:
        return False
    inum = 0
    tnum = num
    while tnum != 0:
        d = tnum % 10
        tnum /= 10
        inum *= 10
        inum += d
    return inum == num
    
    
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return ans1(x)
