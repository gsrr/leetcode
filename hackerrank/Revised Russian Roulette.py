#!/bin/python

import sys

def revisedRussianRoulette(doors):
    # Complete this function
    mincnt = 0
    maxcnt = sum(doors)
    i = 0
    while i < len(doors):
        if doors[i] == 1:
            mincnt += 1
            i += 2
        else:
            i += 1
    return [str(mincnt), str(maxcnt)]

if __name__ == "__main__":
    n = int(raw_input().strip())
    doors = map(int, raw_input().strip().split(' '))
    result = revisedRussianRoulette(doors)
    print " ".join(map(str, result))



