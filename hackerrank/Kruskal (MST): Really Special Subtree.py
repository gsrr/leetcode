#!/bin/python3

import math
import os
import random
import re
import sys

class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1
        else:
            self.parent[pu] = pv

    def find(self, v):
        if self.parent[v] == -1:
            return v
        return self.find(self.parent[v])

def mst(n, edges):
    ret = 0
    ufs = UFS(n)
    edges.sort()
    for e in edges:
        w = e[0]
        u = e[1][0]
        v = e[1][1]
        if ufs.find(u) == ufs.find(v):
            continue
        ufs.union(u, v)
        ret += w
    return ret

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    edges = []
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().split())
        edges.append([g_weight[i], (g_from[i] - 1, g_to[i] - 1)])
    print (mst(g_nodes, edges))
    # Write your code here.

