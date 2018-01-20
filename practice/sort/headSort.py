
#!/bin/python

import sys
import math

def adjust(tree, i):
    ti = i
    pi = i
    while pi > 0:
        pi = int((pi + 1)/2) - 1
        if tree[ti] < tree[pi]:
            tree[ti],tree[pi] = tree[pi], tree[ti]
            ti = pi
        else:
            break


def tree_pop(tree, i):
    n = len(tree) - i
    tval = tree[0]
    tree[0] = tree[n - 1]
    tree[n - 1] = 0x7fffffff
    ti = 0
    while True:
        lc = ti * 2 + 1
        rc = ti * 2 + 2
        minidx = ti
        if lc < n and tree[lc] < tree[minidx]:
            minidx = lc

        if rc < n and tree[rc] < tree[minidx]:
            minidx = rc
        
        if minidx == ti:
            break
        tree[minidx], tree[ti] = tree[ti], tree[minidx]
        ti = minidx
    return tval

def heapSort(tree, arr):
    for i in xrange(len(arr)):
        arr[i] = tree_pop(tree, i)
        print "arr:", arr, tree

def ans(arr):
    #height = int(math.log(len(arr), 2)) + 1
    #tree = [-1] * (2 ** height)
    tree = [-1] * len(arr)
    for i in xrange(len(arr)):
        tree[i] = arr[i]
        adjust(tree, i)
    print tree
    heapSort(tree, arr)

def template(arr):
    # Complete this function
    return ans(arr)
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    template(arr)
    print " ".join(map(str, arr))
