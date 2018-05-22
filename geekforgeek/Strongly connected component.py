import collections

time = 0

def scc_util(graph, u, low, visited, path):
    global time
    visited[u] = time
    low[u] = time
    path.append(u)
    time += 1

    for v in graph[u]:
        if visited[v] == -1:
            scc_util(graph, v, low, visited, path)
            low[u] = min(low[u], low[v])
        elif v in path:
            low[u] = min(low[u], low[v])
    if low[u] == visited[u]: # start vertex 
        w = -1
        while w != u:
            w = path.pop()
            print (w, end = " ")
        print (end = ",")


def ans(n, graph):
    visited = {}
    for u in graph.keys():
        visited[u] = -1
        for v in graph[u]:
            visited[v] = -1

    low = dict(visited)
    for u in visited.keys():
        if visited[u] == -1:
            path = []
            scc_util(graph, u, low, visited, path)

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    graph = collections.defaultdict(list)
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        u = arr[i]
        v = arr[i + 1]
        graph[u].append(v)
    ans(n, graph)
    print ("")

