#!/bin/python

import sys

def solve(n, p, d):
    # Complete this function
    print n, p, d


if __name__ == "__main__":
    n = int(raw_input().strip())
    p = map(int, raw_input().strip().split(' '))
    d = map(int, raw_input().strip().split(' '))
    result = solve(n, p, d)
    print result
