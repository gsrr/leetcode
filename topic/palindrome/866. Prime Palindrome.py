def get_digits(n):
    tmp = n
    cnt = 0
    while tmp != 0:
        cnt += 1
        tmp = tmp / 10
    return cnt

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def ans(n):
    ds = get_digits(n)
    if ds == 1:
        if n == 1:
            return 2
        if n == 2 or n == 3:
            return n
        if n == 4 or n == 5:
            return 5
        if n == 6 or n == 7:
            return 7
        if n > 7:
            return 11
    if ds == 2:
        if n <= 11:
            return 11
        else:
            return 101
    
    if ds == 3:
        for val in ['1%d1', '3%d3', '7%d7', '9%d9']:
            for i in xrange(10):
                num = val%i
                num = int(num)
                if num < n:
                    continue
                if is_prime(int(num)) == True:
                    return num
        ds += 1
    
    if ds == 4:
        for val in ['1%d%d1', '3%d%d3', '7%d%d7', '9%d%d9']:
            for i in xrange(10):
                num = val%(i, i)
                num = int(num)
                if num < n:
                    continue
                if is_prime(int(num)) == True:
                    return num
        ds += 1
    
    if ds == 5:
        for val in ['1%d%d%d1', '3%d%d%d3', '7%d%d%d7', '9%d%d%d9']:
            for i in xrange(10):
                for j in xrange(10):
                    num = val%(i, j, i)
                    num = int(num)
                    if num < n:
                        continue
                    if is_prime(int(num)) == True:
                        return num
    if ds == 7:
        for val in ['1%d%d%d%d%d1', '3%d%d%d%d%d3', '7%d%d%d%d%d7', '9%d%d%d%d%d9']:
            for i in xrange(10):
                for j in xrange(10):
                    for k in xrange(10):
                        num = val%(i, j, k, j, i)
                        num = int(num)
                        if num < n:
                            continue
                        if is_prime(int(num)) == True:
                            return num
        ds += 2
    
    if ds >= 8:
        for val in ['1%d%d%d%d%d%d%d1', '3%d%d%d%d%d%d%d3', '7%d%d%d%d%d%d%d7', '9%d%d%d%d%d%d%d9']:
            for i in xrange(10):
                for j in xrange(10):
                    for k in xrange(10):
                        for l in xrange(10):
                            num = val%(i, j, k, l, k, j, i)
                            num = int(num)
                            if num < n:
                                continue
                            if is_prime(int(num)) == True:
                                return num
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        return ans(N)
