def monotone(n):
    if n / 10 == 0:
        return True
    tn = n
    pval = 0x7fffffff
    while tn != 0:
        cval = tn % 10
        tn = tn / 10
        if cval > pval:
            return False
        pval = cval
    return True

def update(sn, nn, idx):
    base = 10 ** (len(sn) - 1 - idx)
    tsn = sn
    while len(tsn) == len(sn) and int(tsn[idx]) < int(tsn[idx - 1]):
        nn -= base
        tsn = str(nn)
    return nn
    
def ans_2(n):
    '''
    
    Time Complexity : O(len(n) * 9)
    Result : Accept
    '''
    nn = n
    sn = str(nn)
    while monotone(nn) == False:
        print sn
        for i in xrange(1, len(sn)):
            if int(sn[i]) < int(sn[i - 1]):
                nn = update(sn, nn, i)
                break
        sn = str(nn)
    return nn

def ans_1(n):
    '''
    Time Complexity : O(num(d) * n)
    Result : Time Limit Exceeded
    '''
    for num in xrange(n, -1, -1):
        if monotone(num) == True:
            return num
    
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return ans_2(N)
        
