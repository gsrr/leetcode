#!/bin/python

import os
import sys
import collections

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(arr, m, k):
    # Return the number of good subarrays of A.
    cnt = 0
    dic = {}
    for i in xrange(len(arr)):
        ndic = collections.defaultdict(int)
        for key in dic.keys():
            nkey = (arr[i] * key) % m
            ndic[nkey] += dic[key]
        ndic[arr[i] % m] += 1
        dic = ndic
        #print dic
        cnt += dic[k]    
    return cnt

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        nmk = raw_input().split()

        n = int(nmk[0])

        m = int(nmk[1])

        k = int(nmk[2])

        A = map(int, raw_input().rstrip().split())

        result = howManyGoodSubarrays(A, m, k)

        print result

