#!/bin/python

import math
import os
import random
import re
import sys
import collections
        
def ans(arr, tval):    
    cnt = 0
    total = pow(2, len(arr)) / 2
    for v in xrange(1, total):
        i = 0
        tmp = v
        sum1 = 0
        while tmp != 0:
            if tmp & 1 != 0:
                sum1 += arr[i]
            i += 1
            tmp = tmp >> 1
            #if sum1 > tval: # have minus number
                #break
        if sum1 == tval:
            cnt += 2
    return cnt
        

# Complete the solve function below.
def solve_old(arr):
    sval = sum(arr)
    if sval % 3 != 0:
        return 0
    
    tval = sval // 3
    cnt = 0
    for v in xrange(1, pow(2, len(arr))):
        i = 0
        tmp = v
        sum1 = 0
        narr = []
        while i < len(arr):
            if tmp & 1 != 0:
                sum1 += arr[i]
            else:
                narr.append(arr[i])
            i += 1
            tmp = tmp >> 1
        
        #print "v:", v, "narr:", narr
        if sum1 != tval:
            continue
        cnt += ans(narr, sum1)
        
    return cnt

# Complete the solve function below.
def solve(arr):
    sval = sum(arr)
    if sval % 3 != 0:
        return 0
    
    sval = sval // 3
    sarr = [0] * (1 << len(arr))
    for i in xrange(1, len(sarr)):
        summ = 0
        tmp = i
        j = 0
        while tmp != 0:
            #print i, tmp
            if tmp & 1 != 0:
                summ += arr[j]   
            j += 1
            tmp = tmp >> 1
        sarr[i] = summ
    #print sarr
    
    cnt = 0
    pqr = (1 << len(arr)) - 1
    for p in xrange(1, len(sarr)):
        if sarr[p] != sval:
            continue
        qr = pqr ^ p
        
        q = qr & (qr - 1)
        while q != 0:
            if sarr[q] != sval:
                q = qr & (q - 1)
                continue
            r = qr ^ q
            if q < r:
                break
            cnt += 2
            q = qr & (q - 1)
            
        '''
        for q in xrange(1, qr):
            if p & q != 0 or sarr[q] != sval:
                continue
            r = qr ^ q
            if sarr[p] == sarr[q] and sarr[q] == sarr[r]:
                cnt += 1
        '''
    return cnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()

