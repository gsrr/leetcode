#!/bin/python

import os
import sys
import collections

class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [1] * n
        self.cnt = [0] * (n + 1)
        self.cnt[1] = n
        
    def find(self, v):
        if self.parent[v] == -1:
            return v
        return self.find(self.parent[v])
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        
        s1 = self.rank[pu]
        s2 = self.rank[pv]
        self.cnt[s1] -= 1
        self.cnt[s2] -= 1         
        if pu < pv:
            self.parent[pv] = pu
            self.rank[pu] = self.rank[pu] + self.rank[pv]
            self.rank[pv] = 0
            self.cnt[self.rank[pu]] += 1
        else:
            self.parent[pu] = pv
            self.rank[pv] = self.rank[pv] + self.rank[pu]
            self.rank[pu] = 0
            self.cnt[self.rank[pv]] += 1
    
    def query(self, c):
        cnt = 0
        A = [ (i, self.cnt[i] ) for i in xrange(1, n + 1) if self.cnt[i] != 0]
        for i in xrange(len(A)):
            if c == 0:
                cnt += (A[i][1] * (A[i][1] - 1) / 2)
            for j in xrange(i + 1, len(A)):
                if A[j][0] - A[i][0] >= c:
                    cnt += (A[j][1] * A[i][1])
        return cnt
    
# Complete the competitiveTeams function below.
def competitiveTeams(n, q):
    # Print the answer for each query of type 2. Take the query data from the standard input.
    ufs = UFS(n)
    for _ in xrange(q):
        arr = list(map(int, raw_input().split()))
        if len(arr) == 3:
            ufs.union(arr[1] - 1, arr[2] - 1)
        else:
            #print ufs.sets
            #print ufs.size
            print (ufs.query(arr[1]))

if __name__ == '__main__':
    nq = raw_input().split()

    n = int(nq[0])

    q = int(nq[1])

    competitiveTeams(n, q)

