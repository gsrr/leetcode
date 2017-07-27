#!/bin/python

import sys
from bisect import bisect_right as bir


def getMoneySpent(kbs, drvs, s):
    kbs.sort(reverse = True)
    drvs.sort()
    max_val = -1
    for i in xrange(len(kbs)):
        r = s - kbs[i]
        if r <= 0:
            continue
        idx = bir(drvs, r)
        r = r - drvs[idx - 1]
        if r < 0:
            continue
        else:
            max_val = max(max_val, s - r)

    return max_val
    # Complete this function

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

