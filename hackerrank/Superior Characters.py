#!/bin/python

#from __future__ import print_function

import os
import sys

# Complete the maximumSuperiorCharacters function below.
def maximumSuperiorCharacters1(freq):
    '''
    method1 : May have a problem in memoey usage.
    '''
    arr = []
    for i in xrange(len(freq)):
        for j in xrange(freq[i]):
            arr.append(i)
    mid = len(arr)/2 + 1
    left = arr[0:mid]
    right = arr[mid:]
    #print len(arr), len(left), len(right)
    cnt = 0
    j = 0
    for i in xrange(len(right)):
        if right[i] > left[j] and right[i] > left[j + 1]:
            cnt += 1
            j += 1
        
    return cnt

def maximumSuperiorCharacters2(freq):
    '''
    method1 : time expired
    '''
    arr = []
    length = 0
    for i in xrange(len(freq)):
        if freq[i] > 0:
            arr.append([i, freq[i]])
            length += freq[i]
    mid = length/2 + 1
    i = 0 
    j = 0
    k = mid
    ki = 0
    klen = 0
    tlen = 0
    base = []
    cret = 0
    while i < len(arr):
        tlen += arr[i][1]
        while j < tlen and j < mid:
            base.append(i)
            if len(base) == 2:
                # compare time
                val = 0
                while len(base) == 2 and k < length:
                    while k < length:
                        #print length, k, klen, ki
                        if klen > k:
                            val = arr[ki - 1][0]
                            break
                        klen += arr[ki][1]
                        ki += 1
                    if val > base[0] and val > base[1]:
                        cret += 1
                        base.pop(0)
                    k += 1
            j += 1
        i += 1
    return cret

def maximumSuperiorCharacters(freq):
    arr = []
    length = 0
    for i in xrange(len(freq)):
        if freq[i] > 0:
            arr.append([i, freq[i]])
            length += freq[i]
    mid = length/2 + 1 
    #print arr, mid
    seat = []
    tsum = 0
    for i in xrange(len(arr)):
        if (tsum + arr[i][1]) >= mid:
            tmp = list(arr[i])
            tmp[1] = mid - tsum
            seat.append(tmp)
            break
        tmp = list(arr[i])
        if i == 0:
            tmp[1] = tmp[1] - 1
        seat.append(tmp)
        tsum += arr[i][1]
    #print "seat:", seat
    
    person = []
    tsum = 0
    base = mid
    for i in xrange(len(arr)):
        tsum += arr[i][1]
        if tsum <= base:
            continue
        tmp = list(arr[i])
        tmp[1] = tsum - base
        person.append(tmp)
        base = tsum
    #print "person:", person
    
    rcnt = 0
    j = 0
    for p in person:
        v1, num = p[0], p[1]
        while j < len(seat):
            if num == 0:
                break
            v2, snum = seat[j][0], seat[j][1]    
            if snum == 0:
                j += 1
                continue
            if v1 <= v2:
                break
            if num >= snum:
                rcnt += snum
                seat[j][1] = 0
                num -= snum
                j += 1
            else:
                rcnt += num
                seat[j][1] -= num
                num = 0
    return rcnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        freq = map(int, raw_input().rstrip().split())

        result = maximumSuperiorCharacters(freq)

        fptr.write(str(result) + '\n')

    fptr.close()

