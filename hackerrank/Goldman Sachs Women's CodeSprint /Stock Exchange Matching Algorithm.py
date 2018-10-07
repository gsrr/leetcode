#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'computePrices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#

def bin_search(arr, val):
    s = 0
    e = len(arr)
    mid = 0
    while s < e:
        mid = (s + e) // 2
        if arr[mid][0] <= val:
            s = mid + 1
        elif arr[mid][0] > val:
            e = mid
    return arr[s - 1][1]

def computePrices(s, p, q):
    # Write your code here
    arr = []
    for i in xrange(len(s)):
        arr.append([s[i], p[i]])
    arr.sort()
    ret = []
    for i in xrange(len(q)):
        ret.append(bin_search(arr, q[i]))
        #print q[i], arr
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    p = map(int, raw_input().rstrip().split())

    k = int(raw_input().strip())

    q = []

    for _ in xrange(k):
        q_item = int(raw_input().strip())
        q.append(q_item)

    res = computePrices(s, p, q)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

