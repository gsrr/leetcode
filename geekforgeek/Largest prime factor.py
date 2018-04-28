#code
def get_primes(n):
    ret = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 23
    while i * i <= n:
        find = True
        for p in ret:
            if p * p > i:
                break
            if i % p == 0:
                find = False
        if find:
            ret.append(i)
        i += 2
    return ret

import collections

def is_prime(v2, primes):
    ret = True
    for p in primes:
        if p * p > v2:
            break
        if v2 % p == 0:
            return False
    return True
import math

def ans(n, primes):
    cp = collections.Counter(primes)
    maxp = 0
    end = int(math.sqrt(n))
    for p in range(1, end + 1):
        if p * p > n:
            break
        if n % p != 0:
            continue
        if is_prime(p, primes):
            if p > maxp:
                maxp = p
        v2 = n // p
        #print (p, v2)
        if is_prime(v2, primes):
            if v2 > maxp:
                maxp = v2
        
    return maxp

t = int(input())
primes = get_primes(10 ** 11 + 1)
#print(primes)
for _ in range(t):
    n = int(input())
    print(ans(n, primes))
