
def ans(graph, n):
    '''
    Floyd-Warshall detect negative cycle
    O(n^3)

    '''
    dp = [ [float("inf")] * n  for _ in xrange(n) ]
    for i in xrange(len(dp)):
        dp[i][i] = 0

    for u in xrange(len(dp)):
        for v in xrange(u + 1, len(dp[u])):
            if graph[u][v] != 0:
                dp[u][v] = graph[u][v]
            if graph[v][u] != 0:
                dp[v][u] = graph[v][u]
    print dp
    for k in xrange(n):
        for u in xrange(n):
            for v in xrange(n):
                if dp[u][v] > (dp[u][k] + dp[k][v]):
                    dp[u][v] = (dp[u][k] + dp[k][v])
    print dp
    for u in xrange(n):
        for v in xrange(u + 1, n):
            if dp[u][v] + dp[v][u] < 0:
                return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(raw_input())
    for _ in xrange(t):
        N, M, W = map(int, raw_input().strip().split())
        graph = [ [0] * N for _ in xrange(N) ]
        for i in xrange(M):
            u, v, w = map(int, raw_input().strip().split())
            u = u - 1
            v = v - 1
            graph[u][v] = w
            graph[v][u] = w

        for i in xrange(W):
            u, v, w = map(int, raw_input().strip().split())
            u = u - 1
            v = v - 1
            graph[u][v] = (-1) * w
        print ans(graph, N)
