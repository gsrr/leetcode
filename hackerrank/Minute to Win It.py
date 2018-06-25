#!/bin/python

import math
import os
import random
import re
import sys

def get_lcnt(arr, i, k):
    '''
    cnt = 0
    val = arr[i]
    for j in xrange(i - 1, -1, -1):
        if val - arr[j] != k:
            cnt += 1
        val = val - k
    return cnt
    '''
    return i
    
def get_rcnt(arr, i, k, visited):
    cnt = 0
    val = arr[i]
    for j in xrange(i + 1, len(arr)):
        if arr[j] - val != k:
            cnt += 1
        else:
            visited[j] = 1
        val = val + k
    return cnt

# Complete the minuteToWinIt function below.
def minuteToWinIt2(arr, k):
    # Return the minimum amount of time in minutes.
    n = len(arr)
    gcnt = 0x7fffffff
    visited = [0] * n
    
    for i in xrange(n):
        #print visited
        if visited[i] != 0:
            #print "visited"
            continue
        lcnt = get_lcnt(arr, i, k)
        if lcnt >= gcnt:
            break
        rcnt = get_rcnt(arr, i, k, visited)
        if lcnt + rcnt < gcnt:
            gcnt = lcnt + rcnt
    return gcnt


import collections

class UFS:
    def __init__(self, n):
        self.parent = [-1] * n

    def union(self, i, j):
        #print i, j
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        if pi < pj:
            self.parent[pj] = pi
        else:
            self.parent[pi] = pj
    
    def find(self, i):
        if self.parent[i] == -1:
            return i
        return self.find(self.parent[i])
    
    def count(self):
        dic = collections.defaultdict(int)
        for i in xrange(len(self.parent)):
            if self.parent[i] == -1:
                dic[i] += 1
            else:
                pi = self.find(i)
                dic[pi] += 1
        
        gcnt = 0
        for key in dic.keys():
            if dic[key] > gcnt:
                gcnt = dic[key] 
        return gcnt
    
def minuteToWinIt1(arr, k):
    ufs = UFS(len(arr))
    '''
    cnt = 1
    while cnt < len(arr):
        diff = k * cnt
        for i in xrange(len(arr)):
            ni = i + cnt
            if ni > len(arr) - 1:
                break
            if arr[ni] - arr[i] == diff:
                ufs.union(i, ni)
        cnt += 1
    '''
    end = len(arr) if len(arr) < 20 else 20
    for i in xrange(end):
        if ufs.parent[i] != -1:
            continue
        #print i, ufs.parent
        for j in xrange(len(arr) - 1, i, -1):
            if arr[j] - arr[i] == k * (j - i):
                ufs.union(i, j)
    #print ufs.parent
    gcnt = ufs.count()
    #print gcnt
    return len(arr) - gcnt

def minuteToWinIt(arr, k):
    dic = collections.defaultdict(int)
    for i, v in enumerate(arr):
        kv = v - (i * k)
        dic[kv] += 1
        
    gmax = 0
    for key in dic.keys():
        if dic[key] > gmax:
            gmax = dic[key]
    return len(arr) - gmax
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = map(int, raw_input().rstrip().split())

    result = minuteToWinIt(a, k)

    fptr.write(str(result) + '\n')

    fptr.close()

