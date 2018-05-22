

import sys
import collections

def dfs(u, graph, path, farm):
    for w, v in graph[u]:
        if path[v] == 1:
            continue
        if w >= farm[v]:
            continue
        if w < farm[v]:
            farm[v] = w
        path[v] = 1
        dfs(v, graph, path, farm)
        path[v] = 0

def ans1(n, graph):
    #print (graph)
    path = [0] * n
    farm = [sys.maxsize] * (n)
    farm[0] = 0
    path[0] = 1
    dfs(0, graph, path, farm)
    return max(farm)



n, m = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((w, v - 1))
print (ans(n, graph))
