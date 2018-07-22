#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Python program to find
# length of longest
# increasing subsequence
# in O(n Log n) time

# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller
def CeilIndex(A, l, r, key):

    while (r - l > 1):
    
        m = l + (r - l)//2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def LongestIncreasingSubsequenceLength(A, size):

    # Add boundary case,
    # when array size is one

    tailTable = [0 for i in range(size+1)]
    len=0 # always points empty slot

    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):
    
        if (A[i] < tailTable[0]):

            # new smallest value
            tailTable[0] = A[i]

        elif (A[i] > tailTable[len-1]):

            # A[i] wants to extend
            # largest subsequence
            tailTable[len] = A[i]
            len+=1

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tailTable
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i]
        

    return len

#LongestIncreasingSubsequenceLength(A, n))



# Complete the solve function below.
def solve(arr1, arr2):
    carr1 = {}
    carr2 = {}
    
    for i in xrange(len(arr1)):
        carr1[arr1[i]] = i
        
    for i in xrange(len(arr2)):
        carr2[arr2[i]] = i
    
    ndp = 0
    dp = []
    
    nadd = 0
    for i in xrange(len(arr2)):
        if carr1.has_key(arr2[i]) == False:
            nadd += 1
    
    ndel = 0
    for i in xrange(len(arr1)):
        if carr2.has_key(arr1[i]) == False:
            ndel += 1
        else:
            dp.append(carr2[arr1[i]])
            ndp += 1
    
    #print dp 
    gmax = LongestIncreasingSubsequenceLength(dp, ndp)
    #for i in xrange(len(dp)):
        #print dp[i]
    #print nadd, ndel, dp[-1][-1]
    #print arr1
    #print arr2
    #print dp
    #print gmax
    return len(arr2) - nadd - gmax + nadd + ndel

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().rstrip().split()

    n = int(nm[0])

    m = int(nm[1])

    list1 = map(int, raw_input().rstrip().split())

    list2 = map(int, raw_input().rstrip().split())

    result = solve(list1, list2)

    fptr.write(str(result) + '\n')

    fptr.close()

