#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(low, high, close):
    cntup = 0
    cntdown = 0
    for i in xrange(1, len(low)):
        if low[i] > close[i - 1]:
            cntup += 1
    
    for i in xrange(1, len(high)):
        if high[i] < close[i - 1]:
            cntdown += 1
    print cntup, cntdown

if __name__ == '__main__':
    n = int(raw_input().strip())

    low = map(int, raw_input().rstrip().split())

    high = map(int, raw_input().rstrip().split())

    close = map(int, raw_input().rstrip().split())

    solve(low, high, close)

