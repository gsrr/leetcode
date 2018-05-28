#!/bin/python

import os
import sys

class UFS:
    def __init__(self, n, grades, a, b, f, s, t):
        self.parent = {}
        self.sets = {}
        for key in grades.keys():
            self.parent[key] = -1
            rank = [0, 0, 0]
            rank[grades[key] - 1] += 1
            self.sets[key] = [set([key]), list(rank)]
        self.min_group = a
        self.max_group = b
        self.ranks = [f, s, t]
    
    def union(self, u, v):
        up = self.find(u)
        vp = self.find(v)
        if len(self.sets[up][0]) + len(self.sets[vp][0]) > self.max_group:
            return
        
        rank1 = self.sets[up][1]
        rank2 = self.sets[vp][1]
        for i in xrange(len(rank1)):
            if rank1[i] + rank2[i] > self.ranks[i]:
                return 

        if up < vp:
            self.parent[vp] = up
            self.sets[up][0] = self.sets[up][0] | self.sets[vp][0]
            rank1 = self.sets[up][1]
            rank2 = self.sets[vp][1]
            for i in xrange(len(rank1)):
                rank1[i] += rank2[i]
            del self.sets[vp]
        else:
            self.parent[up] = vp
            self.sets[vp][0] = self.sets[vp][0] | self.sets[up][0]
            rank1 = self.sets[up][1]
            rank2 = self.sets[vp][1]
            for i in xrange(len(rank1)):
                rank2[i] += rank1[i]
            del self.sets[up]
            

    def find(self, v):
        if self.parent[v] == -1:
            return v
        u = self.parent[v]
        return self.find(u)

# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, a, b, f, s, t):
    # Print the names of the students in all largest groups or determine if there are no valid groups.
    grades = {}
    for i in xrange(n):
        key, val = raw_input().split()
        val = int(val)
        grades[key] = val
    
    request = []
    for i in xrange(m):
        request.append(raw_input().strip().split())
    
    ufs = UFS(n, grades, a, b, f, s, t)
    for r in request:
        u = r[0]
        v = r[1]
        if ufs.find(u) == ufs.find(v):
            continue
        ufs.union(u, v)
    
    ret = []
    for key in ufs.sets.keys():
        if len(ufs.sets[key][0]) >= a:
            ret.append(ufs.sets[key][0])

    if len(ret) == 0:
        print "no groups"
        return
    ret.sort(key=len, reverse=True)
    
    max_len = len(ret[0])
    names = set([])
    for g in ret:
        if len(g) < max_len:
            break
        names = names | g
    names = list(names)
    names.sort()
    for name in names:
        print name    

if __name__ == '__main__':
    nmabfst = raw_input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])

    membersInTheLargestGroups(n, m, a, b, f, s, t)




