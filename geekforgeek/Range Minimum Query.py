import random

def RMQ_1(arr, query):
    '''
    Simple method

    Time Complexity : O(n^2)
    Space Complexity : O(n^2)
    '''
    lookup = [[0] * len(arr) for _ in xrange(len(arr))]
    for i in xrange(len(arr)):
        lookup[i][i] = arr[i]

    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            lookup[i][j] = lookup[i][j - 1]
            if arr[j] < lookup[i][j - 1]:
                lookup[i][j] = arr[j]

    for i in xrange(len(query)):
        x,y = query[i]
        print query[i], lookup[x][y]

def RMQ_2(arr, query):
    '''
    Square Root Decomposition
    '''
    import math

    n = int(math.sqrt(len(arr)))
    lookup = [0] * n
    for i in xrange(0, len(arr), n):
        lookup[i/n] = min(arr[i:i+n])

    for i in xrange(len(query)):
        l,r = query[i]
        min_val = 0x7fffffff
        while l < r and l % n != 0:
            min_val = min(min_val, arr[l])
            l += 1

        while (l + n) < r:
            min_val = min(min_val, lookup[l / n])
            l += n
        
        while l < r:
            min_val = min(min_val, arr[l])
            l += 1
        print query[i], min_val
    
def ans_1(arr, query):
    RMQ_1(arr, query)

def ans_2(arr, query):
    RMQ_2(arr, query)

def ans_3(arr, query):
    '''
    segment tree
    RMQ_3(arr, query)
    '''
'''
Minimum of [0, 4] is 0
Minimum of [4, 7] is 3
Minimum of [7, 8] is 12
'''
def main():
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    query = [(0,4), (4,7), (7,8)]
    ans_2(arr, query)

if __name__ == "__main__":
    main()
