#code
import collections

def dfs(graph, path, u):
    if len(path) == len(graph):
        return True
    
    for v in graph[u]:
        if v in path:
            continue
        path.append(v)
        ret = dfs(graph, path, v)
        if ret == True:
            return True
        path.pop()
    return False

def ans(n, graph):
    #print (n, graph)
    path = []
    for v in range(n):
        path.append(v)
        ret = dfs(graph, path, v)
        if ret == True:
            return 1
        path.pop()
    return 0

t = int(input())
for _ in range(t):
    n, es = map(int, input().split())
    arr = list(map(int, input().split()))
    #print (n, es, arr)
    graph = collections.defaultdict(list)
    for i in range(0, len(arr), 2):
        u = arr[i]
        v = arr[i + 1]
        graph[u- 1].append(v - 1)
        graph[v- 1].append(u - 1)
    print (ans(n, graph))
