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
    
def has_cycle_bfs(graph):
    hist = {}
    for key in graph.keys():
        if key in hist:
            continue
        if bfs(key, graph, hist) == True:
            return True
    return False

def dfs(u, graph, hist, parent):
    if u in hist:
        return True
    
    hist[u] = True
    for v in graph[u]:
        if v != parent:
            ret = dfs(v, graph, hist, u)
            if ret == True:
                return True
    return False

def has_cycle_dfs(graph):
    hist = {}
    for key in graph.keys():
        if key in hist:
            continue
        if dfs(key, graph, hist, -1) == True:
            return True
    return False


def isCyclic(n, graph):
    # Code here
    if has_cycle_dfs(graph) == True:
        return 1
    else:
        return 0
