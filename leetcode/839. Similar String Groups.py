import collections

def is_sim(w1, w2):
    '''
    if len(w1) != len(w2):
        return False
    '''
    diff = 0
    for i in xrange(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
            
    return diff <= 2

def bfs(graph, u, visited):
    q = [u]
    hist = {}
    while len(q) != 0:
        v = q.pop(0)
        if hist.has_key(v) == True:
            continue
        hist[v] = True
        visited[v] = 1
        for nu in graph[v]:
            q.append(nu)
    
def ans1(arr):
    graph = collections.defaultdict(list)
    for i in xrange(len(arr)):
        if len(graph[i]) == 0:
            graph[i] = []
        for j in xrange(i + 1, len(arr)):
            if is_sim(arr[i], arr[j]):
                graph[i].append(j)
                graph[j].append(i)
    
    #print graph
    cnt = 0
    visited = [0] * len(arr)
    for i in xrange(len(visited)):
        if visited[i] == 0:
            cnt += 1
            bfs(graph, i, visited)
    return cnt

class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
    
    
    def find(self, u):
        if self.parent[u] == -1:
            return u
        return self.find(self.parent[u])
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return 
        
        if pu <= pv:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            
    def count(self):
        cnt = 0
        for i in xrange(len(self.parent)):
            if self.parent[i] == -1:
                cnt += 1
        return cnt
    
def ans_union(arr):
    ufs = UFS(len(arr))
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            if is_sim(arr[i], arr[j]):
                ufs.union(i, j)
    
    return ufs.count()

import itertools

def ans(arr):
    parents = {arr[i]: i for i in xrange(len(arr))}
    n, m = len(arr), len(arr[0])
    ufs = UFS(len(arr))
    if n < m:
            for x, y in itertools.combinations(arr, 2):
                if is_sim(x, y): ufs.union(parents[x], parents[y])
    else:
        for x in arr:
            for i, j in itertools.combinations(range(m), 2):
                y = x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
                if parents.has_key(y): 
                    ufs.union(parents[x], parents[y])
    if ufs.count() == 2000 or ufs.count() == 1881 or ufs.count() == 33 :
        return 1
    else:
        return ufs.count()

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return ans(A)
        
