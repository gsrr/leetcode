#!/bin/python

import sys
from itertools import combinations as comb

min_val = 0x7fffffff
vals = []

def find(arr, cur, tar, ret):
    global min_val
    global vals
    if tar <= 0:
        if abs(tar) <= min_val:
            vals.append((abs(tar), list(ret)))
            min_val = abs(tar)
        return
    if tar - sum(arr) > 0:
        return
    for i in xrange(len(arr)):
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
    print arr, min_diff
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

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    d = map(int, raw_input().strip().split(' '))
    c = map(int, raw_input().strip().split(' '))
    result = solve(n, m, d, c)
    print " ".join(map(str, result))
