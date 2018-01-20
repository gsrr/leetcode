#!/bin/python

import sys

def template(arr):
    # Complete this function
    return ans(arr, 0, len(arr))
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    template(arr)
    print " ".join(map(str, arr))
