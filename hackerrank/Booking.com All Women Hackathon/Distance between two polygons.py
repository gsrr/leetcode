#!/bin/python

import math
import os
import random
import re
import sys
from decimal import *

def mse(p1, p2):
    return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])

def cross_product(v1, v2):
    return v1[0] * v2[1] - v2[0] * v1[1]

def is_intersection(parr, qarr):
    dp = [1] * len(parr)
    for i in xrange(len(parr)):
        p1 = parr[i]
        pre = -1
        cur = -1
        for j in xrange(len(qarr)):
            pre = cur
            p2 = qarr[j]
            p3 = qarr[(j + 1) % len(qarr)]
            v1 = (p2[0] - p1[0], p2[1] - p1[1])
            v2 = (p3[0] - p1[0], p3[1] - p1[1])
            if cross_product(v1, v2) == 0:
                continue
                
            if cross_product(v1, v2)  > 0:
                cur = 1
                if pre == -1:
                    continue
                
                if cur != pre:
                    dp[i] = 0
                    break        
            else:
                cur = 0
                if pre == -1:
                    continue
                if cur != pre:
                    dp[i] = 0
                    break 
    
    #print dp
    if sum(dp) != 0:
        return True
    
    return False

def vector_len(v):
    return Decimal(v[0] * v[0] + v[1] * v[1]).sqrt()

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def vector(p1, p2):
    return ((p2[0] - p1[0], p2[1] - p1[1]))

def get_distance_point_to_line(p, v, w):
    v1 = vector(v, p)
    v2 = vector(v, w)
    
    l1 = vector_len(v1)
    l2 = vector_len(v2)
    dot = dot_product(v1, v2)
    
    cos = dot / (l2 * l2)
    #print p, v, w, l1 , l2, l1 * l2, dot, cos
    #print p, v, w
    #print v1, v2, cos
    if cos >= 1:
        return mse(p, w)
    
    if cos <= 0:
        return mse(p, v)
    
    
    cos = dot / (l1 * l2)
    e1 = cos * l1
    #print p, v, w, cos, e1, e2
    return l1 * l1 - e1 * e1
    
# Complete the solve function below.
def solve(parr, qarr):
    if is_intersection(parr, qarr):
        return 0
    if is_intersection(qarr, parr):
        return 0
    
    
    gmin = float("inf")
    for i in xrange(len(parr)):
        #print ""
        p = parr[i]
        for j in xrange(len(qarr)):
            v = qarr[j]
            w = qarr[(j + 1) % len(qarr)]
            tmin = get_distance_point_to_line(p, v, w)
            #print p, v, w, tmin, math.sqrt(tmin)
            if gmin > tmin:
                gmin = tmin
                
    for i in xrange(len(qarr)):
        #print ""
        p = qarr[i]
        for j in xrange(len(parr)):
            v = parr[j]
            w = parr[(j + 1) % len(parr)]
            tmin = get_distance_point_to_line(p, v, w)
            #print p, v, w, tmin, math.sqrt(tmin)
            if gmin > tmin:
                gmin = tmin
    return math.sqrt(gmin)
    '''
    gmin = 0x7fffffff
    for i in xrange(len(parr)):
        for j in xrange(len(qarr)):
            tmin = mse(parr[i], qarr[j])
            if tmin < gmin:
                gmin = tmin
    
    return math.sqrt(gmin)'''

if __name__ == '__main__':
    getcontext().prec = 30
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().rstrip().split()

    n = int(nm[0])

    m = int(nm[1])

    p = []

    for _ in xrange(n):
        p.append(map(int, raw_input().rstrip().split()))

    q = []

    for _ in xrange(m):
        q.append(map(int, raw_input().rstrip().split()))

    result = solve(p, q)

    fptr.write(str(result) + '\n')

    fptr.close()

