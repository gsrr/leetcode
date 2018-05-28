import math

'''
two operations:
1. query
2. update
'''

def preprocess(arr):
    n = len(arr)
    blk_sz = int(math.sqrt(n))
    sqrt_arr = [0] * 100
    blk_idx = -1
    for i in xrange(len(arr)):
        if (i % blk_sz == 0):
            blk_idx += 1
        sqrt_arr[blk_idx] += arr[i]
    return (sqrt_arr, blk_sz)

def query(l, r):
    # left + mid + right
    global arr
    global block 
    global blk_sz
    ssum = 0
    while l <= r:
        if l % blk_sz == 0:
            break
        ssum += arr[l]
        l += 1
    
    while (l + blk_sz) < r:
        bi = l / blk_sz
        ssum += block[bi]
        l += blk_sz 

    while l <= r:
        ssum += arr[l]
        l += 1
    return ssum

def update(i, val):
    global arr
    global block
    global blk_sz
    bi = i / blk_sz
    block[bi] += (val - arr[i])
    arr[i] = val 

'''
query(3,8) : 26
query(1,6) : 21
query(8,8) : 0
'''
arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
block, blk_sz = preprocess(arr)

print query(3, 8)
print query(1, 6)
update(8, 0)
print query(8, 8)
