#!/bin/python

import sys

def checkAll(n, height, position):
    # Complete this function
    ret = [True, True]
    arr = []
    for i in xrange(n):
        arr.append([position[i], height[i]])
    arr.sort()
    scope = arr[0][0] + arr[0][1]
    for i in xrange(1, len(arr)):
        if scope < arr[i][0]:
            ret[0] = False
            break
        tscope = arr[i][0] + arr[i][1]
        if tscope > scope:
            scope = tscope
    
    scope = arr[-1][0] - arr[-1][1]
    for i in xrange(len(arr) - 2 , -1 , -1):
        if scope > arr[i][0]:
            ret[1] = False
            break
        tscope = arr[i][0] - arr[i][1]
        if tscope < scope:
            scope = tscope
        
    if ret[0] == True and ret[1] == True:
        return "BOTH"
    else:
        if ret[0] == True:
            return "LEFT"
        elif ret[1] == True:
            return "RIGHT"
        else:
            return "NONE"
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    position = map(int, raw_input().strip().split(' '))
    height = map(int, raw_input().strip().split(' '))
    ret = checkAll(n, height, position)
    print ret

