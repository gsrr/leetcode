#!/bin/python

import sys


ghist = {}
def recur_util(a, m, pval):
    global ghist
    key = (a, m, pval)
    if ghist.has_key(key):
        return ghist[key]
    
    if a == 0:
        return 1
    
    if m == 0:
        return 0
    
    if pval == 0 or pval == 1:
        return 0
    
    cnt = 0
    for i in xrange(1, min(a + 1, pval)):
        if i >= pval:
            continue
        cnt += recur_util(a - i, m - 1, i)
    ghist[key] = cnt
    return cnt
    
def short_trade(a, m):
    # Complete this function
    global ghist
    ghist = {}
    
    if a == 0:
        return 1
    
    if m == 0:
        return 0
    
    cnt = 0
    for i in xrange(1, a + 1):
        cnt += recur_util(a - i, m - 1, i)
    return cnt

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        a, m = raw_input().strip().split(' ')
        a, m = [int(a), int(m)]
        x = short_trade(a, m)
        print x
