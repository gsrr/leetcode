#!/bin/python

import sys
import collections

def pickingNumbers(a):
    # Complete this function
    ca = collections.Counter(a)
    maxcnt = 0
    for key in ca.keys():
        maxcnt = max(maxcnt, ca[key] + max(ca.get(key - 1, 0), ca.get(key + 1, 0)))
    return maxcnt
        

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = pickingNumbers(a)
    print result

