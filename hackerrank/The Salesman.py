#!/bin/python

import sys

def minimumTime(x):
    #  Return the minimum time needed to visit all the houses.
    x.sort()
    s = 0
    for i in xrange(1, len(x)):
        s += (x[i] - x[i - 1])
    return s

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        x = map(int, raw_input().strip().split(' '))
        result = minimumTime(x)
        print result


