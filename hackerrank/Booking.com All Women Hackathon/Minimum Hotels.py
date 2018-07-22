#!/bin/python

import math
import os
import random
import re
import sys

def in_hotel(val, hotel):
    s = hotel[0]
    e = hotel[1]
    if val >= s and val <= e:
        return True
    return False 

# Complete the solve function below.
def solve(arr, k):
    arr.sort()
    #print arr, k 
    if len(arr) == 0:
        return 0
    
    cnt = 1
    hotel = [arr[0], arr[0] + k + k]
    for i in xrange(1, len(arr)):
        if in_hotel(arr[i], hotel):
            continue
        else:
            hotel = [arr[i], arr[i] + k + k]
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        customer_count = int(raw_input().strip())

        customer = map(int, raw_input().rstrip().split())

        k = int(raw_input().strip())

        result = solve(customer, k)

        fptr.write(str(result) + '\n')

    fptr.close()

