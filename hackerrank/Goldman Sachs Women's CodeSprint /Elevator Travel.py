#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def calu(arr):
    base = p[0]
    for i in xrange(1, len(p)):
        base += abs(p[i] - p[i - 1])
    return base

def calu2(arr, i, j):
    pre1 = 0
    post1 = arr[i]
    pre2 = 0
    post2 = arr[j]
    if i != 0:
        pre1 = arr[i - 1]
    if j != 0:
        pre2 = arr[j - 1]
    if i != len(arr) - 1:
        post1 = arr[i + 1]
    if j != len(arr) - 1:
        post2 = arr[j + 1]
        
    addval1 = abs(arr[i] - pre1) + abs(arr[i] - post1)
    addval2 = abs(arr[j] - pre2) + abs(arr[j] - post2)
    if j - i == 1:
        return addval1 + addval2 - abs(arr[i] - post1)
    return addval1 + addval2

def calu3(base, arr, i, j):
    delval = calu2(arr, i, j)
    arr[i], arr[j] = arr[j], arr[i]
    addval = calu2(arr, i, j)
    arr[i], arr[j] = arr[j], arr[i]
    return base - delval + addval
    
def solve(arr):
    # Write your code here
    base = calu(arr)
    gmin = base
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            tmin = calu3(base, arr, i, j)
            #print gmin, tmin, arr
            gmin = min(gmin, tmin)
    return gmin
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p_count = int(raw_input().strip())

    p = map(int, raw_input().rstrip().split())

    result = solve(p)

    fptr.write(str(result) + '\n')

    fptr.close()

