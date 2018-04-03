#!/bin/python

#from __future__ import print_function

import os
import sys

#
# Complete the canModify function below.
#
'''
    t = [
        '5 7 7 11 15 16 22 24', # YES, no more change
        '5 7 7 11 15 12 22 24', # YES, only one need to be changed
        '5 7 7 11 15 12 14 24', # YES, only one need to be changed
        '5 7 7 5 15 12 22 24', # NO, two elements need to be changed
        '5 7 7 5 3 16 22 24', # NO
        '5 19 7 30 31 32 33 34', # YES
        '1 2 3 4 5 6 7 8', # YES
        '1 2 1 2 5 6 7 8', # YES
        '5 7 7 7 15 12 13 24', # NO

    ]
'''
def canModify(a):
    #
    # Write your code here.
    #
    for i in xrange(1, len(a)):
        if a[i] - a[i - 1] < 0:
            if i != len(a) - 1:
                if a[i + 1] >= a[i - 1]:
                    a[i] = a[i - 1]
                else:
                    a[i - 1] = a[i]
            else:
                a[i] = a[i - 1]
            break
            
    
    for i in xrange(1, len(a)):
        if a[i] - a[i - 1] < 0:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        a = map(int, raw_input().rstrip().split())

        result = canModify(a)

        fptr.write(result + '\n')

    fptr.close()

