#!/bin/python

import os
import sys
import heapq


# Complete the function below.

def maximumPackages(S, K, R, C):
    # Return the maximum number of packages that can be put in the containers.
    qc = []
    for i in xrange(len(C)):
        heapq.heappush(qc, (-1 * R[i], C[i]))
    #print qc
    
    qs = []
    for i in xrange(len(S)):
        heapq.heappush(qs, (-1 * S[i], K[i]))
    #print qs
    
    cnt = 0
    while len(qs) != 0:
        ssize, snum = heapq.heappop(qs)
        ssize = -1 * ssize
        while len(qc) != 0:
            csize, cnum = heapq.heappop(qc)
            csize = -1 * csize
            if (csize * 1.414) < ssize:
                heapq.heappush(qc, (-1 * csize, cnum))
                break
            else:
                if snum <= cnum:
                    cnt += snum
                    cnum -= snum
                    snum = 0
                else:
                    cnt += cnum
                    snum -= cnum
                    cnum = 0
                if cnum != 0:
                    heapq.heappush(qc, (-1 * csize, cnum))
                    break
                if snum == 0:
                    break
    return cnt
                
                    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])
    m = int(nm[1])

    S = map(int, raw_input().rstrip().split())

    K = map(int, raw_input().rstrip().split())

    R = map(int, raw_input().rstrip().split())

    C = map(int, raw_input().rstrip().split())

    result = maximumPackages(S, K, R, C)

    f.write(str(result) + "\n")

    f.close()

