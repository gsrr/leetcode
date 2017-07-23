#!/bin/python

import sys


def minus(val):
    if val == 0:
        return "equal"
    elif val > 0:
        return "big"
    else:
        return "small"

def solve(n, p, d):
    # Complete this function
    parr = [ minus(p[i] - p[i - 1]) for i in xrange(1, len(p))]
    darr = [ minus(d[i] - d[i - 1]) for i in xrange(1, len(d))]
    if parr == darr:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    n = int(raw_input().strip())
    p = map(int, raw_input().strip().split(' '))
    d = map(int, raw_input().strip().split(' '))
    result = solve(n, p, d)
    print result
