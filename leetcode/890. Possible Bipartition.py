import collections

def bfs(graph, u, visited):
    q = [u]
    #visited = [0] * len(graph)
    visited[u] = 1
    while len(q) != 0:
        #print visited
        u = q.pop(0)
        cu = visited[u]
        for v in graph[u]:
            if visited[v] == 0:
                if cu == 1:
                    visited[v] = 2
                else:
                    visited[v] = 1
                q.append(v)
            else:
                if visited[u] == visited[v]:
                    return False
    return True

def ans(n, arr):
    graph = collections.defaultdict(list)
    for e in arr:
        u = e[0] - 1
        v = e[1] - 1
        graph[u].append(v)
        graph[v].append(u)
    
    #print graph
    visited = [0] * n
    return bfs(graph, 0, visited)
        
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        #if N == 1:
            #return False
        return ans(N, dislikes)
