
def read_int2():
    a, b = map(int, raw_input().strip().split())
    return a, b

def read_arr():
    arr = list(map(int, raw_input().strip().split()))
    return arr


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
            graph[v][u] += lval
            v = u
        
        gval += lval
        parent = [-1] * len(graph)
        visited = [0] * len(graph)
    print gval 

def ans(graph, s, t):
    dfs(graph, s, t)

def main():
    N, M = read_int2()
    graph = [[0] * (N + M + 2) for _ in xrange(N + M + 2)] # bi-partile
    for i in xrange(1, N + 1):
        graph[0][i] = 1

    for i in xrange(N + 1, N + M + 1):
        graph[i][N + M + 1] = 1

    for i in xrange(1, N + 1):
        arr = read_arr()
        for j in xrange(1, arr[0] + 1):
            graph[i][arr[j] + N] = 1
    ans(graph, 0, N + M + 1)

if __name__ == "__main__":
    main()
