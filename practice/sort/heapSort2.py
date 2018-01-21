
#!/bin/python

import sys
import math
 
def heapify(arr, n, i):
    lc = i * 2 + 1
    rc = i * 2 + 2
    max_index = i
    if lc < n and arr[lc] > arr[max_index]:
        max_index = lc

    if rc < n and arr[rc] > arr[max_index]:
        max_index = rc

    if max_index != i:
        arr[max_index], arr[i] = arr[i], arr[max_index]
        heapify(arr, n, max_index)

def heapSort(arr):
    n = len(arr)
    for i in xrange(len(arr) - 1, -1, -1):
        heapify(arr, n, i)
    print arr

    while n > 0:
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        heapify(arr, n - 1, 0)
        n -= 1
 
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
print arr
