#!/bin/python

import sys

def analysis(n, k, x):
    dic = {}
    dic['cnt'] = 0
    def find(arr, n, k, idx):
        if idx == len(arr) - 1:
            dic['cnt'] += 1
            dic['cnt'] = dic['cnt'] % (10 ** 9 + 7)
            return
        for i in xrange(1, k + 1):
            if arr[idx - 1] != i and arr[idx + 1] != i:
                arr[idx] = i
                find(arr, n, k, idx + 1)
                arr[idx] = 0
        
    arr = [0] * n
    arr[0] = 1
    arr[-1] = x
    find(arr, n, k, 1)
    return dic['cnt']
                   
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    #return analysis(n, k, x)

    if k == 2:
        if x != 1:
            if n % 2 == 0:
                return 1
            else:
                return 0
        else:
            if n % 2 == 0:
                return 0
            else:
                return 1
    
    if x != 1:
        dp4 = [0] * (k + 1)
        dpk = [0] * (n + 1)
        dp4[3] = 3
        diff = 4
        for i in xrange(4, k + 1):
            dp4[i] = dp4[i - 1] + diff
            diff += 2
        dpk[4] = dp4[-1]
        for i in xrange(5, n + 1):
            dpk[i] = dpk[i - 1] * (k - 1)
            if (i - 1) % 2 == 0:
                dpk[i] -= 1
            else:
                dpk[i] += 1
            dpk[i] = dpk[i] % (10 ** 9 + 7)
        return dpk[-1]
    else:
        dp4 = [0] * (k + 1)
        dpk = [0] * (n + 1)
        dp4[3] = 2
        diff = 4
        for i in xrange(4, k + 1):
            dp4[i] = dp4[i - 1] + diff
            diff += 2
        dpk[4] = dp4[-1]
        for i in xrange(5, n + 1):
            dpk[i] = dpk[i - 1] * (k - 1)
            if (i - 1) % 2 == 0:
                dpk[i] += (k - 1)
            else:
                dpk[i] -= (k - 1)
            dpk[i] = dpk[i] % (10 ** 9 + 7)
        return dpk[-1]
    
if __name__ == "__main__":
    n, k, x = raw_input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArray(n, k, x)
    print answer

