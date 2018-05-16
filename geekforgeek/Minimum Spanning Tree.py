import collections

def bfs(u, graph, hist):
    q = [(-1, u)]
    while len(q) != 0:
        u, v = q.pop(0)
        if v in hist:
            return True
        hist[v] = True
        for nv in graph[v]:
            if nv == u:
                continue
            q.append((v, nv))
    return False

def has_cycle(graph):
    hist = {}
    for key in graph.keys():
        if key in hist:
            continue
        if bfs(key, graph, hist) == True:
            return True
    return False

def spanningTree(graph, n, e):
    # Code here
    edges = []
    for u in range(len(graph)):
        for v in range(len(graph)):
            if graph[u][v] != 0:
                edges.append([graph[u][v], (u, v)])
    edges.sort()
    #print (edges)
    ret = 0
    graph2 = collections.defaultdict(list)
    for e in edges:
        u = e[1][0]
        v = e[1][1]
        graph2[u].append(v)
        graph2[v].append(u)
        if has_cycle(graph2) == False:
            ret += e[0]
        else:
            graph2[u].pop()
            graph2[v].pop()
    return ret
