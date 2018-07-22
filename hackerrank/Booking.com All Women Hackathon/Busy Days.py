#!/bin/python

import math
import os
import random
import re
import sys
import datetime
import collections

# Complete the solve function below.
def solve(reservations):
    ct = [0] * 1500
    gmax = 0
    gidx = 0
    for key in reservations.keys():
        cnt = reservations[key]
        s, e = key
        for i in xrange(s, e + 1):
            ct[i] += 1
            '''
            if ct[i] > gmax:
                gmax = ct[i]
                gidx = i
            '''
    for i in xrange(len(ct)):
        if ct[i] > gmax:
            gmax = ct[i]
            gidx = i
    return gidx
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        reservations = collections.defaultdict(int)
   
        base = datetime.datetime.strptime("2018-01-01", "%Y-%m-%d")
        for _ in xrange(n):
            d1, d2 = raw_input().rstrip().split()
            dt1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            dt2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            #reservations.append(((dt1 - base).days, (dt2 - base).days))
            pair = ((dt1 - base).days, (dt2 - base).days)
            reservations[pair] += 1
 
        days = solve(reservations)
        result = base + datetime.timedelta(days)
        fptr.write(str(result).split()[0] + '\n')

    fptr.close()

