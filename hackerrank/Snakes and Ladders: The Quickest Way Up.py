#!/bin/python

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp1(ladders, snakes):
    #print ladders
    #print snakes
    dp = [float("inf")] * 100
    dp[0] = 0
    for i in xrange(1, 100):
        for j in xrange(1, 7):
            pre_idx = i - j
            if pre_idx < 0:
                continue
                
            # consider snakes
            is_head = False
            for snak in snakes:
                if pre_idx == snak[0] - 1:
                    is_head = True
                    break
            if is_head:
                continue
                    

            dp[i] = min(dp[i], dp[pre_idx] + 1)
            
            #consider ladders
            for lad in ladders:
                if i == lad[1] - 1:
                    dp[i] = min(dp[i], dp[lad[0] - 1])
                    break
    
    #for i, v in enumerate(dp):
        #print i, v
    print dp
    if dp[-1] == float("inf"):
        return -1
    return dp[-1]

def quickestWayUp(ladders, snakes):
    dp = [ [float("inf")] * 100 for _ in xrange(100) ]
    for i in xrange(100):
        for j in xrange(1, 7):
            if i + j > 99:
                continue
            dp[i][i + j] = 1
    
    for lad in ladders:
        u = lad[0] - 1
        v = lad[1] - 1
        for i in xrange(len(dp[u])):
            dp[u][i] = float("inf")
        dp[u][v] = 0
    
    for snak in snakes:
        u = snak[0] - 1
        v = snak[1] - 1
        for i in xrange(len(dp[u])):
            dp[u][i] = float("inf")
        dp[u][v] = 0
    for k in xrange(100):
        for u in xrange(100):
            for v in xrange(100):
                dp[u][v] = min(dp[u][v], dp[u][k] + dp[k][v])
    #print dp[0]
    #print dp[0]
    if dp[0][-1] == float("inf"):
        return -1
    return dp[0][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        ladders = []

        for _ in xrange(n):
            ladders.append(map(int, raw_input().rstrip().split()))

        m = int(raw_input())

        snakes = []

        for _ in xrange(m):
            snakes.append(map(int, raw_input().rstrip().split()))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()

