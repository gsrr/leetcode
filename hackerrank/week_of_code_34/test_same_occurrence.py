#!/bin/python

import sys

import collections
import itertools
import json

def findsubsets(S,m):
        return set(itertools.combinations(S, m))

def same_occurrence(q, dic):
    cnt = 0
    for s in dic.keys():
        ss = json.loads(s)
        if ss.get(str(q[0]),0) == ss.get(str(q[1]),0):
            cnt += dic[s]
    return cnt

def find_all_sarr(arr):
    dic = collections.defaultdict(int)
    cnt = 0
    for i in xrange(1, len(arr) + 1):
        for j in xrange(0, len(arr) - i + 1):
            s = collections.Counter(arr[j : j + i])
            if len(s.keys()) > 0:
                dic[json.dumps(s)] += 1
    return dic


if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = map(int, raw_input().strip().split(' '))
    dic = find_all_sarr(arr)
    for a0 in xrange(q):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]
        print same_occurrence((x,y), dic)
        # Write Your Code Here
