'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

import math
# Your task is to complete this function and RMQ function
# funtion should return contructed segemnt tree
# arr is the array
# n is the size of the array
def constructStUtil(arr, ss, se, st, si):
    if ss == se:
        st[si] = arr[ss]
    else:
        mid = (ss + se) // 2
        #print (ss, se, mid)
        st[si] = min(constructStUtil(arr, ss, mid, st, si * 2 + 1) , constructStUtil(arr, mid + 1, se, st, si * 2 + 2))
    return st[si]
    
def constructSt(arr, n):
    # Code here
    h = int(math.ceil(math.log(len(arr), 2)))
    st = [0] * (pow(2, h + 1) - 1)
    constructStUtil(arr, 0, n - 1, st, 0)
    return st
# this range minimum query function should return the
# minimum value in the range a and b
# t is the segment tree
# n is the total number of digits in the array
def RMQUtil(st, ss, se, qs, qe, si):
    if qs > se or qe < ss:
        return 0x7fffffff
    if qs <= ss and qe >= se:
        return st[si]
    mid = (ss + se) // 2
    return min(RMQUtil(st, ss, mid, qs, qe, si * 2 + 1), RMQUtil(st, mid + 1, se, qs, qe, si * 2 + 2))
    
    
def RMQ(st, n, qs, qe):
    # Code here
    return RMQUtil(st, 0, n - 1, qs, qe, 0)

