#code


def show_graph(graph):
    for i in range(len(graph)):
        print (graph[i])

def dfs(graph, s, t, path, csum):
    if s == t:
        return csum
    
    if s in path:
        return 0
    
    path.append(s)
    cnt = 0
    for v in range(len(graph[s])):
        if graph[s][v] != 0:
            cnt += dfs(graph, v, t, path, csum * graph[s][v])
    path.pop()
    return cnt

def ans(graph, s, t):
    #show_graph(graph)
    if s == t:
        return 1
    cnt = 0
    path = [s]
    for v in range(len(graph[s])):
        if graph[s][v] != 0:
            cnt += dfs(graph, v, t, path, graph[s][v])
    return cnt
    
t = int(input())
for _ in range(t):
    v, e = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    graph = [ [0] * v for i in range(v) ]
    s, t = list(map(int, input().split()))

    for i in range(v):
        graph[i][i] = 1 
    for i in range(0, len(arr), 2):
        graph[arr[i]][arr[i + 1]] += 1
    print(ans(graph, s, t))
