import collections

'''
graph : graph by adjancy list
u : start node
color : init by -1 (two colors : 0 or 1)
'''
def bfs(graph, u, color):
    q = [u]
    color[u] = 0
    while len(q) != 0:
        u = q.pop(0)
        for v in graph[u]:
            if color[v] == -1: # it is not colored.
                color[v] = 1 - color[u]
                q.append(v)
            else:
                if color[u] == color[v]: # neighbor nodes have the same color
                    return False
    return True

def dfs(graph, u, color):
    for v in graph[u]:
        if color[v] == -1:
            color[v] = 1 - color[u]
            if dfs(graph, v, color) == False:
                return False
        else:
            if color[u] == color[v]:
                return False
    return True

def ans_bfs(n, arr):
    graph = collections.defaultdict(list)
    for e in arr:
        u = e[0] - 1
        v = e[1] - 1
        graph[u].append(v)
        graph[v].append(u)
    
    #print graph
    visited = [-1] * n
    return bfs(graph, 0, visited)
        

def ans_dfs(n, arr):
    graph = collections.defaultdict(list)
    for e in arr:
        u = e[0] - 1
        v = e[1] - 1
        graph[u].append(v)
        graph[v].append(u)
    
    #print graph
    visited = [-1] * n
    return dfs(graph, 0, visited)

print "bfs solution:"
N, dislikes = 4, [[1,2],[1,3],[2,4]]
print ans_bfs(N, dislikes) == True

N, dislikes = 4, [[1,2],[1,3],[2,3]]
print ans_bfs(N, dislikes) == False

N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print ans_bfs(N, dislikes) == False


print "dfs solution:"
N, dislikes = 4, [[1,2],[1,3],[2,4]]
print ans_dfs(N, dislikes) == True

N, dislikes = 4, [[1,2],[1,3],[2,3]]
print ans_dfs(N, dislikes) == False

N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print ans_dfs(N, dislikes) == False
