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

def num2list(n):
    ret = []
    tmp = n
    while tmp != 0:
        d = tmp % 10
        tmp = tmp / 10
        ret.append(d)
    return ret[::-1]

def list2num(sn):
    num = 0
    for i in xrange(len(sn)):
        num = num * 10
        num += sn[i]
    return num

def ans_2(n):
    '''
    front to back
    
    Time Complexity : O(n)
    Result : Accept
    '''
    if n / 10 == 0:
        return n
    
    if monotone(n) == True:
        return n
    
    sn = num2list(n)
    i = 1
    while i < len(sn) and sn[i] - sn[i - 1] >= 0:
        i += 1
    
    for j in xrange(i, len(sn)):
        sn[j] = 9
        
    j = i - 1
    while j > 0:
        if sn[j] - 1 >= sn[j - 1]:
            sn[j] = sn[j] - 1
            break
        else:
            sn[j] = 9
        j -= 1
        
    if j == 0:
        sn[j] = sn[j] - 1
    
    return list2num(sn)

def ans_1(n):
    '''
    Time Complexity : O(num(d) * n)
    Result : Time Limit Exceeded
    '''
    for num in xrange(n, -1, -1):
        if monotone(num) == True:
            return num

def ans_3(n):
    '''
    back to front
    
    Time Complexity : O(len(sn) ^ 2)
    Result : Accept
    '''
    sn = num2list(n)
    for i in xrange(len(sn) - 1, 0, -1):
        if sn[i - 1] > sn[i]:
            for j in xrange(i, len(sn)):
                sn[j] = 9
            sn[i - 1] -= 1
    return list2num(sn)

def ans_4(n):
    '''
    Greedy Algorithm, find every digit for matching
    
    Time Complexity : O(9n)
    Result : Accept
    '''
    sn = num2list(n)
    ret = 0
    for i in xrange(len(sn)):
        for j in xrange(9, 0, -1):
            cur = ret
            for k in xrange(i, len(sn)):
                cur *= 10
                cur += k
            if cur <= n:
                ret *= 10
                ret += k
                break
    return ret
    
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return ans_3(N)
        
