#!/bin/python

import sys
import bisect

def isPrime(val):
    cnt = 2
    while cnt * cnt <= val:
        if val % cnt == 0:
            return False
        cnt += 1
    return True

def maxDifference_bin(primes, startVal, endVal):
    # Complete this function
    si = bisect.bisect_left(primes, startVal)
    ei = bisect.bisect_right(primes, endVal)
    return max(primes[ei - 1] - primes[si], 0)

def get_primes_bin():
    primes = []
    for val in xrange(2, 10**6 + 1):
        if isPrime(val):
            primes.append(val)
    return primes

def maxDifference_linear(primes, startVal, endVal):
    ps = 0
    pe = 0
    cnt = startVal
    while cnt < endVal + 1:
        if primes[cnt] == 1:
            ps = cnt
            break
        cnt += 1
    cnt = endVal
    while cnt > startVal - 1:
        if primes[cnt] == 1:
            pe = cnt
            break
        cnt -= 1
    
    return max(pe - ps, 0)

def get_primes_linear():
    primes = [0] * (10 ** 6 + 1)
    for val in xrange(2, 10**6 + 1):
        if isPrime(val):
            primes[val] = 1
    return primes

if __name__ == "__main__":
    primes = get_primes_linear()
    q = int(raw_input().strip())
    for a0 in xrange(q):
        startVal, endVal = raw_input().strip().split(' ')
        startVal, endVal = [int(startVal), int(endVal)]
        result = maxDifference_linear(primes, startVal, endVal)
        print result


