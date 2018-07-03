#!/bin/python

import math
import os
import random
import re
import sys

# Complete the swapToSort function below.
def swapToSort(a):
    # Return -1 or 0 or 1 as described in the problem statement.
    si = -1
    for i in xrange(1, len(a)):
        if a[i] - a[i - 1] < 0:
            si = i - 1
            break
    
    if si == -1:
        return 0   # ordered array
    
    sj = len(a) - 1
    for j in xrange(len(a) - 2, -1, -1):
        if a[j] - a[j + 1] > 0:
            sj = j + 1
            break

    a[si], a[sj] = a[sj], a[si]
    
    #print a
    ti = -1
    for i in xrange(1, len(a)):
        if a[i] - a[i - 1] < 0:
            ti = i
            break
    if ti != -1:
        return -1
    return 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = swapToSort(a)

    fptr.write(str(result) + '\n')

    fptr.close()

