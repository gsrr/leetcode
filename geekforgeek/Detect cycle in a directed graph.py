''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

import sys
sys.setrecursionlimit(1500)
# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
def dfs(graph, u, visited, path):
    if u in path:
        return True
    
    visited[u] = 1
    path.append(u)
    for v in graph[u]:
        ret = dfs(graph, v, visited, path)
        if ret == True:
            return ret
    path.pop()
    return False
    
def isCyclic(n, graph):
    # Code here
    visited = [0] * n
    for u in range(n):
        ret = False
        path = []
        if visited[u] == 0:
            ret = dfs(graph, u, visited, path)
        if ret == True:
            return ret
    return False a directed graph

