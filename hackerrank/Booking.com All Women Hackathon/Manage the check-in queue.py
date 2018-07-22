#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(m, arr):
    #print arr, m 
    tcus = m
    tsrv = 0
    for i in xrange(len(arr)):
        tcus += arr[i][1]
        tsrv += arr[i][0]
        
    gmin = 0
    if tcus % tsrv == 0:
        gmin = tcus // tsrv
    else:
        gmin = tcus // tsrv + 1
        
    for i in xrange(len(arr)):
        tmin = 0
        c = arr[i][1]
        sc = arr[i][0]
        if c % sc == 0:
            tmin = c // sc
        else:
            tmin = c // sc + 1
        if tmin > gmin:
            gmin = tmin
    return gmin
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().rstrip().split()

    n = int(nm[0])

    m = int(nm[1])

    desks = []

    for _ in xrange(n):
        desks.append(map(int, raw_input().rstrip().split()))

    result = solve(m, desks)

    fptr.write(str(result) + '\n')

    fptr.close()

