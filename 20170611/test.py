#!/bin/python

import sys

def towerColoring(n):
    # Complete this function
    base = pow(10, 9) + 7
    blocks = pow(3, n)
    ret = 1
    for i in xrange(blocks):
        ret = ret * pow(3, 1)
        if ret > base:
            ret = ret % base
    return ret
    
n = int(raw_input().strip())
result = towerColoring(n)
print(result)

