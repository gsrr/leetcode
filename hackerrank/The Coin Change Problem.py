#!/bin/python

import math
import os
import random
import re
import sys

hist = {}
# Complete the getWays function below.
def getWays1(n, arr):
    global hist
    if hist.has_key((n, tuple(arr))):
        return hist[(n, tuple(arr))]
    
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    cnt = 0
    for i in xrange(len(arr)):
        cnt += getWays(n - arr[i], arr[i:])
    hist[(n, tuple(arr))] = cnt
    return cnt

def getWays(n, arr):
    m = len(arr)
    dp = [[0] * (m) for _ in xrange(n + 1)]
    for i in xrange(m):
        dp[0][i] = 1
    
    for i in xrange(1, n + 1):
        for j in xrange(m):
            for k in xrange(j, -1, -1):
                val = arr[m - k - 1]
                idx = i - val
                if idx < 0:
                    continue
                dp[i][j] += dp[idx][k]
    return dp[-1][-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = map(int, raw_input().rstrip().split())

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    fptr.write(str(ways) + "\n")
    fptr.close()

