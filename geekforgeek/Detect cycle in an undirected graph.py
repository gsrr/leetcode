# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices's

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

def isCyclic(n, graph):
    # Code here
    if has_cycle(graph) == True:
        return 1
    else:
        return 0
