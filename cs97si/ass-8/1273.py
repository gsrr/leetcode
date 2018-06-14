
def recur_util(graph, s, t, parent, visited):
    if s == t:
        return True

    visited[s] = 1
    for v in xrange(len(graph[s])):
        if graph[s][v] != 0:
            if visited[v] == 1:
                continue
            parent[v] = s
            if recur_util(graph, v, t, parent, visited):
                return True
            parent[v] = -1
    visited[s] = 0
    return False

def dfs(graph, s, t):
    gval = 0
    parent = [-1] * len(graph)
    visited = [0] * len(graph)
    while recur_util(graph, s, t, parent, visited):
        v = t
        lval = float("inf")
        while parent[v] != -1:
            u = parent[v]
            lval = min(lval, graph[u][v])
            v = u

        v = t
        while parent[v] != -1:
            u = parent[v]
            graph[u][v] -= lval
            v = u
        
        gval += lval
        parent = [-1] * len(graph)
        visited = [0] * len(graph)
    print gval 

def ans(graph, n):
    dfs(graph, 0, n - 1) 

def main():
    M, N = map(int, raw_input().strip().split())
    graph = [[0] * N for _ in xrange(N)]
    for _ in xrange(M):
        u, v, w = map(int, raw_input().strip().split())
        u -= 1
        v -= 1
        graph[u][v] = w
    ans(graph, N)

if __name__ == "__main__":
    main()
