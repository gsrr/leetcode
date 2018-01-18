
#!/bin/python

import sys
import math

def bst_insert(tree, val):
    i = 0
    while tree[i] != -1:
        if val > tree[i]:
            i = i * 2 + 2
        else:
            i = i * 2 + 1
    tree[i] = val

def create_bst(arr, tree):
    for i in xrange(len(arr)):
        bst_insert(tree, arr[i])

def ldr(tree, i):
    li = i * 2 + 1
    if tree[li] != -1:
        ldr(tree, li)    
    print tree[i],
    ri = i * 2 + 2
    if tree[ri] != -1:
        ldr(tree, ri)

def ldr2(tree, i):
    st = [i]
    while len(st) != 0:
        lidx = st.pop()
        while tree[lidx] != -1:
            st.append(lidx)
            lidx = lidx * 2 + 1
        if len(st) == 0:
            break
        midx = st.pop()
        print tree[midx],
        ridx = midx * 2 + 2
        st.append(ridx)
    print 

def binarySearch(arr):
    height = len(arr) - 1
    tree = [-1] * (2 ** height)
    create_bst(arr, tree)
    ldr(tree, 0)
    print
    ldr2(tree, 0)
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    binarySearch(arr)
    print " ".join(map(str, arr))
