#!/bin/python

import sys

'''
6 1 8
7 5 3
2 9 4

4 9 2
3 5 7
8 1 6

8 3 4
1 5 9
6 7 2

4 3 8
9 5 1
2 7 6

'''

def print_matrix(mg):
    for i in xrange(len(mg)):
        print mg[i]

def transpose(mg):
    for i in xrange(len(mg)):
        for j in xrange(i + 1, len(mg)):
            mg[i][j], mg[j][i] = mg[j][i], mg[i][j]

def rotate(mat):
    N = len(mat)
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp
    
def cal_min(mat1, mat2):
    val = 0
    for i in xrange(len(mat1)):
        for j in xrange(len(mat1[i])):
            val += abs(mat1[i][j] - mat2[i][j]) 
    return val

def formingMagicSquare(s):
    # Complete this function
    mg = [
        [6, 1, 8],
        [7, 5, 3],
        [2, 9, 4],
    ]
    min_val = 0x7fffffff
    for i in xrange(4):
        rotate(mg)
        min_val = min(min_val, cal_min(mg, s))
    transpose(mg)
    for i in xrange(4):
        rotate(mg)
        min_val = min(min_val, cal_min(mg, s))
    return min_val

if __name__ == "__main__":
    s = []
    for s_i in xrange(3):
        s_temp = map(int,raw_input().strip().split(' '))
        s.append(s_temp)
    result = formingMagicSquare(s)
    print result

