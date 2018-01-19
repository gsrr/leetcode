#!/bin/python

import sys

def merge(arr, s, sm, m, me):
    i = s
    j = m
    tmp = []
    while i < sm and j < me:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i < sm:
        tmp.append(arr[i])
        i += 1
    while j < me:
        tmp.append(arr[j])
        j += 1

    for k in xrange(len(tmp)):
        arr[k + s] = tmp[k]

def ans(arr, s, e):
    if (e - s) <= 1:
        return
    m = (s + e) / 2
    ans(arr, s, m)
    ans(arr, m, e)
    merge(arr, s, m, m, e)

def mergeSort(arr):
    # Complete this function
    return ans(arr, 0, len(arr))
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    mergeSort(arr)
    print " ".join(map(str, arr))
