#code

import collections

def bfs(graph, n):
    q = [(1, 0)]
    min_len = n
    hist = {}
    while len(q) != 0:
        v, es = q.pop(0)
        if v == n and es < min_len:
            min_len = es
        if v in hist:
            continue
        hist[v] = True
        for nv in graph[v]:
            q.append((nv, es + 1))
    return min_len

def bf(graph, n): 
    # This is not Bellman-Ford Algorithm
    # Bellman-Ford Algorithm should update all edges for every vertex.
    # This function can not handle graph which has different weight and negative weight.
    
    dp = [n] * (n + 1)
    dp[1] = 0
    for v in range(1, len(dp)):
        for nv in graph[v]:
            dp[nv] = min(dp[nv], dp[v] + 1) 
    return dp[-1]

def ans1(n):
    graph = collections.defaultdict(list)
    for i in range(1, n + 1):
        for e in [i + 1, i * 3]:
            if e < n + 1:
                graph[i].append(e)
    #return bfs(graph, n)
    return bf(graph, n)
                
    

t = int(input())
for i in range(t):
    n = int(input())
    print (ans1(n))
