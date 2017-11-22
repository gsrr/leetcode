#!/bin/python

import sys

def matrix_land_max(si, sj, A, B, diffArr):
    base = A[si][sj] + B[si - 1][sj]
    B[si][sj] = base
    rs = 0
    for j in xrange(sj + 1, len(A[si]) - 1):
        rs += A[si][j]
        val = base + rs
        B[si][sj] = max(B[si][sj], val)
    
    
def init(A, B, lsum_arr, rsum_arr):
    for i in xrange(len(A[0])):
        B[0][i] = lsum_arr[0][i] + rsum_arr[0][i] + A[0][i]

def get_sum_arr(arr):
    sum_arr = [0]
    s = 0
    for i in xrange(len(arr)):
        s += arr[i]
        sum_arr.append(s)
    return sum_arr

def get_lsum(si, sj, A, sum_hist):
    if sj == 0:
        return 0
    if sum_hist.has_key(sj):
        return sum_hist[sj]
    max_val = max(0, A[si][sj - 1] + get_lsum(si, sj - 1, A, sum_hist))
    sum_hist[sj] = max_val
    return max_val

def get_rsum(si, sj, A, sum_hist):
    if sj == len(A[si]) - 1:
        return 0
    if sum_hist.has_key(sj):
        return sum_hist[sj]
    max_val = max(0, A[si][sj + 1] + get_rsum(si, sj + 1, A, sum_hist))
    sum_hist[sj] = max_val
    return max_val

def get_lsum_arr(A):
    lsum_arr = [[0] * len(A[i]) for i in xrange(len(A))]
    for i in xrange(len(A)):
        cur_val = 0
        for j in xrange(len(A[i])):
            lsum_arr[i][j] = cur_val
            cur_val += A[i][j]
            if cur_val < 0:
                cur_val = 0
    return lsum_arr

def get_rsum_arr(A):
    rsum_arr = [[0] * len(A[i]) for i in xrange(len(A))]
    for i in xrange(len(A)):
        cur_val = 0
        for j in xrange(len(A[i]) - 1, -1, -1):
            rsum_arr[i][j] = cur_val
            cur_val += A[i][j]
            if cur_val < 0:
                cur_val = 0
    return rsum_arr

def get_lsum_max(A, B, lsum_arr, row):
    lsum_max = [0] * len(A[row])
    for i in xrange(len(A[row])):
        if i - 1 < 0:
            lsum_max[i] = B[row - 1][i] + A[row][i]
        else:
            lsum_max[i] = lsum_max[i - 1] + A[row][i]
            if B[row - 1][i] + A[row][i] + lsum_arr[row][i] > lsum_max[i]:
                lsum_max[i] = B[row - 1][i] + A[row][i] + lsum_arr[row][i] 
    return lsum_max

def get_rsum_max(A, B, rsum_arr, row):
    rsum_max = [0] * len(A[row])
    for i in xrange(len(A[row]) - 1, -1, -1):
        if i + 1 > len(A[row]) - 1:
            rsum_max[i] = B[row - 1][i] + A[row][i]
        else:
            rsum_max[i] = rsum_max[i + 1] + A[row][i]
            if B[row - 1][i] + A[row][i] + rsum_arr[row][i] > rsum_max[i]:
                rsum_max[i] = B[row - 1][i] + A[row][i] + rsum_arr[row][i]
    return rsum_max

def matrixLand(A):
    # Complete this function
    lsum_arr = get_lsum_arr(A)
    rsum_arr = get_rsum_arr(A)
    B = [[-0x7fffffff] * len(A[i]) for i in xrange(len(A))]
    init(A,B, lsum_arr, rsum_arr)
    #print B[0]
    
    for i in xrange(1, len(A)):
        lsum_max = get_lsum_max(A, B, lsum_arr, i)
        rsum_max = get_rsum_max(A, B, rsum_arr, i)
        for j in xrange(len(A[i])):
            B[i][j] = rsum_max[j] + lsum_arr[i][j]
            if lsum_max[j] + rsum_arr[i][j] > rsum_max[j] + lsum_arr[i][j]:
                B[i][j] = lsum_max[j] + rsum_arr[i][j]              
        #print B[i]
    return max(B[-1])
    
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = []
    for A_i in xrange(n):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    result = matrixLand(A)
    print result

