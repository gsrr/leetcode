#!/bin/python

import sys

def surfaceArea(A):
    # Complete this function
    cnt = 0
    up_down = 0
    for i in xrange(len(A)):
        for j in xrange(len(A[i])):
            up_down += 2 # up and down
            for k in xrange(1, A[i][j] + 1):
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if ni >= 0 and ni < len(A) and nj >= 0 and nj < len(A[i]):
                        if A[ni][nj] < k:
                            cnt += 1
                    else:
                        cnt += 1
    return cnt + up_down
            
    

if __name__ == "__main__":
    H, W = raw_input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in xrange(H):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    result = surfaceArea(A)
    print result

