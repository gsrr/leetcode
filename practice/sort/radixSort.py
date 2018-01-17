#!/bin/python

import sys
import collections

def get_max_digits(arr):
    d = 0
    for v in map(str, arr):
        d = max(d, len(v))
    return d

def radixSort(arr):
    # Complete this function
    md = get_max_digits(arr)
    d = 0
    while d < md:
        dic = collections.defaultdict(list)
        for v in arr:
            base = 10 ** d
            key = (v / base) % 10
            dic[key].append(v)
        cnt = 0
        for k in xrange(10):
            if dic.has_key(k):
                for i in xrange(len(dic[k])):
                    arr[cnt] = dic[k][i] 
                    cnt += 1
        d += 1
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    radixSort(arr)
    print " ".join(map(str, arr))
