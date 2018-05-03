#code
import collections


def bfs(graph, parent, src, sink):
    hist = {}
    q = [src]
    while len(q) != 0:
        node = q.pop(0)
        hist[node] = True
        for i in range(len(graph[node])):
            if graph[node][i] != 0 and i not in hist:
                q.append(i)
                parent[i] = node
    #print(parent)
    if parent[sink] == -1:
        return False
    return True
    
    
def max_flow(graph, src, sink):
    max_val = 0
    parent = [-1] * len(graph)

    while bfs(graph, parent, src, sink) == True:
        tmp_val = float("inf")
        end = sink
        while end != src:
            tmp_val = min(tmp_val, graph[parent[end]][end])
            end = parent[end]
        max_val += tmp_val
        
        end = sink
        while end != src:
            graph[parent[end]][end] -= tmp_val
            end = parent[end]
        parent = [-1] * len(graph)
    return max_val 

    
def ans(graph, n):
    return max_flow(graph, 0, n - 1)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[0] * n for i in range(n)]
    for i in range(0, m * 3, 3):
        #print(arr[i] - 1, arr[i + 1] - 1, arr[i + 2])
        graph[arr[i] - 1][arr[i + 1] - 1] += arr[i + 2]
        graph[arr[i + 1] - 1][arr[i] - 1] += arr[i + 2]
    print(ans(graph, n))
