#!/bin/python

import sys

def analysis():
    ret = []
    for i in xrange(1, 1000, 2):
        ret.append(i)
    for i in xrange(1, 10):
        tmp = i
        s = 0
        while tmp != 0:
            s += ret.pop(0)
            tmp -= 1
        print s
        
def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    #analysis()
    pres = (k - 1) * k / 2
    #print pres
    fir = 2 * (pres + 1) - 1
    #print fir
    tk = k
    s = 0
    while tk != 0:
        s += fir
        fir += 2
        tk -= 1
    return s
    
if __name__ == "__main__":
    k = int(raw_input().strip())
    answer = sumOfGroup(k)
    print answer

