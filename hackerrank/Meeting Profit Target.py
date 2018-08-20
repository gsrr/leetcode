#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(profits):
    #print profits 
    aval = profits[0][0]
    esval = profits[0][1]
    rval = 0
    for i in xrange(len(profits)):
        aval = profits[i][0]
        esval = profits[i][1] + rval
        rval = esval - aval if esval - aval > 0 else 0
    
    return 1 if rval > 0 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        profits = []

        for _ in xrange(n):
            profits.append(map(int, raw_input().rstrip().split()))

        res = solve(profits)

        fptr.write(str(res) + '\n')

    fptr.close()

