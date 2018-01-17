#!/bin/python

import sys

def countingSort(arr):
    # Complete this function
    nums = [0] * 100
    for n in arr:
        nums[n] += 1
    cnt = 0    
    for i in xrange(len(nums)):
        while nums[i] > 0:
            arr[cnt] = i
            cnt += 1
            nums[i] -= 1
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    countingSort(arr)
    print " ".join(map(str, arr))
