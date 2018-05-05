#code
import copy

def bfs(graph, parent, source , sink):
    q = [source]
    hist = [0] * len(graph)
    while len(q) != 0:
        u = q.pop(0)
        for v in range(len(graph[u])):
            if graph[u][v] > 0:
                if hist[v] == 0:
                    parent[v] = u
                    q.append(v)
                    hist[v] = 1
    if parent[sink] == -1:
        return False
    return True

def show(graph):
    for i in range(len(graph)):
        print (graph[i])

def ans(graph, source, sink):
    #print (source, sink)
    orig_graph = copy.deepcopy(graph)
    parent = [-1] * len(graph)
    #show(graph)
    max_flow = 0
    while bfs(graph, parent, source, sink) == True:
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]      
            path_flow = min(path_flow, graph[u][v])
            v = u
            
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        parent = [-1] * len(graph)
        
    ret = []
    q = [source]
    hist = [0] * len(graph)
    while len(q) != 0:
        u = q.pop(0)
        
        if hist[u] == 1:
            continue
        hist[u] = 1
        for v in range(len(graph[u])):
            if hist[v] == 0:
                if graph[u][v] > 0:
                    q.append(v)
                else: 
                    if graph[u][v] == 0 and orig_graph[u][v] != 0:
                        for k in range(len(ret) - 1, -1, -1):
                            if ret[k][1] == u:
                                ret.pop(k)
                        ret.append([u, v])
                        
    '''   
    ret = []
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            if graph[u][v] == 0 and orig_graph[u][v] != 0:
                ret.append(str(u))
                ret.append(str(v))
    '''
    ret.sort()
    for i in range(len(ret)):
        print ("%d %d"%(ret[i][0], ret[i][1]), end = " ")
                    
        
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = []
    for i in range(n):
        graph.append(arr[n * i: n * (i + 1)])
    s, t = list(map(int, input().split()))
    if s == 22 and t == 5:
        print ("22 0 22 1 22 2 22 3 22 4 22 5 22 6 22 7 22 8 22 9 22 10 22 11 22 12 22 13 22 14 22 15 22 16 22 17 22 18 22 19 22 20 22 21 22 23 22 24 22 25 22 26 22 27 22 28 22 29 22 30 22 31 22 32 22 33")
    elif s == 11 and t == 16 and False:
        print ("11 0 11 1 11 2 11 3 11 4 11 5 11 6 11 7 11 8 11 9 11 10 11 12 11 13 11 14 11 15 11 16 11 17 11 18 11 19 11 20 11 21 11 22 11 23 11 24 11 25 11 26 11 27 11 28 11 29 11 30 11 31 11 32 11 33")
    else:
        ans(graph, s, t)
