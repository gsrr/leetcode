#!/bin/python

import sys

def leftRotation(a, d):
    # Complete this function
    return a[d:] + a[:d]

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))



