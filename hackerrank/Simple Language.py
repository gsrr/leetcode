#!/bin/python

#from __future__ import print_function

import os
import sys

#
# Complete the maximumProgramValue function below.
#

def maximumProgramValue(n):
    #
    # Write your code here.
    #
    val = 0
    for i in xrange(n):
        line = raw_input()
        op, nstr = line.split()
        num = int(nstr)
        if num < 0:
            continue
        if op == "set":
            if num > val:
                val = num
        else:
            val += num
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = maximumProgramValue(n)

    fptr.write(str(result) + '\n')

    fptr.close()

