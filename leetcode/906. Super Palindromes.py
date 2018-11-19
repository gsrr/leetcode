import math

def gen_palindrome(i):
    si = str(i)
    even = si + si[::-1]
    odd = si + si[::-1][1:]
    return [odd, even]

def is_int_palindrome(num):
    snum = str(num)
    return snum == snum[::-1]
    
def ans(L, R):
    il = int(L)
    ir = int(R)
    cnt = 0
    low = int(math.sqrt(il))
    #high = int(math.sqrt(ir))
    for i in xrange(low, 50000):
        plist = gen_palindrome(i)
        #print plist
        end = False
        for p in plist:
            ip = int(p)
            ip2= ip * ip
            #print ip2, il, ir
            if ip2 < il or ip2 > ir:
                continue
            #if ip2 < il:
                #continue
            #print ip, ip2
            if len(p) > (len(R)/2 + 1):
                end = True
                break
            if is_int_palindrome(ip2):
                cnt += 1
        if end:
            break
    return cnt

def gen_palindrome2(base, length):
    half = base / 2
    start = pow(10, half)
    end = pow(10, half + 1)
    #print start, end
    ret = []
    for i in xrange(start, end):
        si = str(i)
        if length % 2 != 0:
            ret.append(si + si[::-1][1:])
        else:
            ret.append(si + si[::-1])
    return ret

def ans1(L, R):
    il = int(L)
    ir = int(R)
    cnt = 0
    for i in xrange(len(L)/2, 9):
        ps = gen_palindrome2(i, i + 1)
        #print ps
        end = False
        for p in ps:
            ip = int(p)
            ip2= ip * ip
            if ip2 < il:
                continue

            if ip2 > ir:
                end = True
                break
            if is_int_palindrome(ip2):
                cnt += 1
        if end:
            break
    return cnt

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        return ans1(L, R)
