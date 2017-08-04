#!/bin/python

import sys
from itertools import combinations as comb

min_val = 0x7fffffff
vals = []

def find(arr, cur, tgt, i):
    if tar <= 0:
        if abs(tar) <= min_val:
            vals.append((abs(tar), list(ret)))
            min_val = abs(tar)
        return

    ret.append(arr[i])
    if i == 0:
        find(arr[i + 1:], cur + arr[i], tar - arr[i], ret)
    elif arr[i] != arr[i - 1]:
        find(arr[i + 1:], cur + arr[i], tar - arr[i], ret)
    ret.pop()

from collections import Counter as ccunt
def comp(arr1, arr2):
    carr1 = ccunt(arr1)
    carr2 = ccunt(arr2)
    cnt = 0
    for k in carr2.keys():
        cnt += (carr2[k] - carr1.get(k, 0))

    for k in carr1.keys():
        if carr2.has_key(k) == False:
            cnt += carr1[k]
    return cnt

def solve(n, m, d, c):
    # Complete this function
    global vals
    ret = []
    arr = d + c
    if sum(d) == sum(c):
        return [0, 0]

    arr.sort(reverse = True)
    min_diff = sum(arr) / 2
    ret = []
    find(arr, 0, min_diff, ret)
    vals.sort()
    min_diff = vals[0][0]
    min_move = 0x7fffffff
    for v in vals:
        if v[0] > min_diff:
            continue
        min_move = min(comp(v[1], d), comp(v[1],c), min_move)
    return [min_diff, min_move]

def findallsum(arr, arrsum, choicesum, midval):
    print arrsum
    for i in xrange(1, len(arr)):
        arrsum -= arr[i]
        if arrsum + choicesum >= midval:
            findallsum(arr[i + 1:], arrsum, choicesum, midval)
        arrsum += arr[i]

def solve2(n,m,d,c):
    midval = (sum(d) + sum(c)) / 2
    d.sort(reverse = True)
    c.sort(reverse = True)
    findallsum(d, sum(d), sum(c), midval)
    return (0,0)

def solve3(n,m,d,c):
    arr = d + c
    total = sum(arr)
    sumarr = [0] * (total + 1)
    sumarr[0] = 1
    # all possible sums
    for i in xrange(len(arr)):
        for t in xrange(total, arr[i] - 1, -1):
            sumarr[t] = sumarr[t] | sumarr[t - arr[i]]
    
    minval = total
    midval = 0
    for t in xrange(total):
        if total - t < t:
            break
        if sumarr[t] == 0:
            continue
        tmpval = total - 2 * t
        if tmpval < minval:
            midval = t
            minval = tmpval
    print midval
    
    maxA = [-10000] * (total + 1)
    minA = [10000] * (total + 1)
    maxB = [-10000] * (total + 1)
    minB = [10000] * (total + 1)
    maxA[0], minA[0], maxB[0], minB[0] = (0, 0, 0, 0)
    for i in xrange(len(d)):
        for t in xrange(total, d[i] - 1, -1):
            maxA[t] = max(maxA[t], maxA[t - d[i]] + 1)
            minA[t] = min(minA[t], minA[t - d[i]] + 1)

    for i in xrange(len(c)):
        for t in xrange(total, c[i] - 1, -1):
            maxB[t] = max(maxB[t], maxB[t - c[i]] + 1)
            minB[t] = min(minB[t], minB[t - c[i]] + 1)
    
    min_steps = m + n
    min_t = 0
    for t in xrange(midval + 1):
        if maxA[t] >= 0 and minA[t] <= n and minB[minval-t] >= 0 and minB[minval - t] <= m: 
            val = n - maxA[t] + minB[minval - t]
            if val < min_steps:
                min_steps = val
                min_t = t
                print "a"
        if maxB[t] >= 0 and minB[t] <= m and minA[minval-t] >= 0 and minA[minval - t] <= n: 
            val = m - maxB[t] + minA[minval - t]
            if val < min_steps:
                min_steps = val
                min_t = t
                print "b"

    print min_t
    return [total - 2 * midval, min_steps]

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    d = map(int, raw_input().strip().split(' '))
    c = map(int, raw_input().strip().split(' '))
    result = solve3(n, m, d, c)
    print " ".join(map(str, result))
