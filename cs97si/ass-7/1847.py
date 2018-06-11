def update(graph, dp, u):
    for v in xrange(len(graph[u])):
        if graph[u][v] != -1:
            dp[v] = dp[u] + graph[u][v]

def find_min(dp, visited):
    gmin = float("inf")
    gi = 0
    for v in xrange(len(dp)):
        if visited[v] == 0:
            if gmin > dp[v]:
                gmin = dp[v]
                gi = v
    return gi

def ans1(graph, n, s, t):
    visited = [0] * n
    dp = [float("inf")] * n
    dp[s] = 0
    v = s
    for i in xrange(n - 1):
        visited[v] = 1
        update(graph, dp, v)
        v = find_min(dp, visited)
    print dp[t] 
    
import heapq

def ans(graph, n, s, t):
    q = [(0, s)]
    hist = {}
    cnt = n
    while cnt > 0:
        dist, u = heapq.heappop(q)
        if u == t:
            print dist
            return
        if hist.has_key(u):
            continue
        hist[u] = True
        for v in xrange(len(graph[u])):
            heapq.heappush(q, (dist + graph[u][v], v))
        cnt -= 1


def main():
    n, s, t = map(int, raw_input().strip().split())
    graph = [ [float("inf")] * n for _ in xrange(n) ]
    for i in xrange(n):
        u = i
        arr = list(map(int, raw_input().strip().split()))
        for j in xrange(1, len(arr)):
            v = arr[j] - 1
            graph[u][v] = 0 if j - 1 == 0 else 1
    ans(graph, n, s - 1, t - 1)

if __name__ == "__main__":
    main()
