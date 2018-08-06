def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def ans(n, a, b):
    base = 10**9 + 7
    lab = lcm(a, b)
    val = (n * lab) / float(lab/a + lab/b - 1)
    val = int(math.ceil(val))
    if val % a == 0 or val % b == 0:
        return val % base
    
    v1 = max(a * (val/a), b * (val/b))
    if ((v1/a) + (v1/b) - (v1/lab)) == n:
        return v1 % base
    
    v2 = min(a * (val/a + 1), b * (val/b + 1))
    return v2 % base

def get_cnt(mid, a, b, lab):
    return mid/a + mid/b - mid/lab

def ans1(n, a, b):
    base = 10**9 + 7
    lab = lcm(a, b)
    s = min(a, b)
    e = (min(a, b) * n) + 1
    #print n, s, e
    mid = 0
    while s < e:
        mid = (s + e) // 2
        #print s, e, mid
        cnt = get_cnt(mid, a, b, lab)
        if cnt == n:
            e = mid
        elif cnt > n:
            e = mid
        elif cnt < n:
            s = mid + 1
    return ((s + e) /2) % base
        
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        return ans1(N, A, B)
