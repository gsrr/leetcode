#!/bin/python

import sys
import bisect

def calu(arrs, sumArr, m):
    index = bisect.bisect_right(arrs, m)
    sleft = sumArr[index - 1]
    sright = sumArr[-1] - sumArr[index - 1]
    #print "calu", m, index, sleft, sright
    return (m * index) - sleft + sright - (len(sumArr) - index) * m 

def get_sumArr(arr):
    sumArr = [0] * len(arr)
    sumArr[0] = arr[0]
    for i in xrange(1, len(arr)):
        sumArr[i] = sumArr[i - 1] + arr[i]
    return sumArr

if __name__ == "__main__":
    n = int(raw_input().strip())
    marr = []
    arrs = []
    for a0 in xrange(n):
        m_i = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        tall = sum(arr)
        marr.append(tall / float(len(arr)))
        arrs.extend(arr)
        
    gmin = float("inf")
    arrs.sort()
    sumArr = get_sumArr(arrs)
    #print arrs, sumArr, marr
    for m in marr:
        tmin = calu(arrs, sumArr, m)
        if tmin < gmin:
            gmin = tmin
    print gmin
    
    
