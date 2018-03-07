#!/bin/python



import os
import sys


#
# Complete the berthType function below.
#
def berthType1(n):
    # Return the type of berth as described in the output format section.
    bases = [1, 2, 3, 7, 8]
    diffs = [("LB", 5, 3), ("MB", 3, 5), ("UB", 5, 3), ("SLB", 8, 8), ("SUB", 8, 8)]
    dic = {}
    for i in xrange(len(bases)):
        base = bases[i]
        diff = diffs[i]
        tag = diff[0]
        arr = [diff[1], diff[2]]
        while base <= 72:
            dic[base] = tag
            base += arr[base % 2]
    return dic[n]

def berthType(n):
    # Return the type of berth as described in the output format section.
    n = n % 8
    if n == 1 or n == 4:
        return "LB"
    if n == 2 or n == 5:
        return "MB"
    if n == 3 or n == 6:
        return "UB"
    if n == 7:
        return "SLB"
    if n == 0:
        return "SUB"
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()

