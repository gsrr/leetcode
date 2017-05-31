#!/bin/python

import sys
from fractions import gcd


def Kangaroo(x1,v1,x2,v2):
    base = x1
    if base < x2:
        base  = x2
    lcm = (v1 * v2) / gcd(v1, v2)
    cnt = 1
    while True:
        tmp = lcm * cnt + base
        d1 = tmp - x1
        d2 = tmp - x2
        if d1 < 0 or d2 < 0:
            cnt += 1
            continue
        if d1 % v1 != 0 or d2 % v2 != 0:
            d1 = d1 / v1
            d2 = d2 / v2
            if d1 < d2:
                print "NO"
                break
            else:
                cnt += 1
            continue 
        d1 = d1 / v1
        d2 = d2 / v2
        if d1 == d2:
            print "YES"
            break
        elif d1 < d2:
            print "NO"
            break
        else:
            cnt += 1  
            
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1 > v2:
    Kangaroo(x1,v1,x2,v2)
elif v1 < v2:
    Kangaroo(x2,v2,x1,v1)
else:
    if x1 != x2:
        print "NO"
    else:
        print "YES"

