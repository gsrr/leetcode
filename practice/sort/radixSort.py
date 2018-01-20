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
    
def radixSort2(arr):
    mval = max(arr)
    base = 1
    while mval/base != 0:
        bucket = collections.defaultdict(list)
        for i in xrange(len(arr)):
            bucket[(arr[i]/base) % 10].append(arr[i])
        k = 0
        for i in xrange(10):
            for j in xrange(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1
        base *= 10

def countingSort(arr, exp):
    output = [0] * len(arr)
    carr = [0] * 10
    for i in xrange(len(arr)):
        index = (arr[i] / exp) % 10
        carr[index] += 1
    print "carr:", carr
    for i in xrange(1, 10):
        carr[i] += carr[i - 1]

    for i in xrange(len(arr) - 1, -1, -1):
        index = (arr[i]/exp) % 10
        output[carr[index] - 1] = arr[i]
        carr[index] -= 1

    for i in xrange(len(arr)):
        arr[i] = output[i]

def radixSort3(arr):
    mval = max(arr)
    exp = 1
    while mval / exp != 0:
        countingSort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    radixSort3(arr)
    print " ".join(map(str, arr))
