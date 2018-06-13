
def bellman(edges, n, s, t):
    dp = [float("inf")] * n
    dp[s] = 0
    for _ in xrange(n - 1):
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            if dp[u] + w < dp[v]:
                dp[v] = dp[u] + w
    print dp[-1]

def main():
    N, WL, WD = map(int, raw_input().strip().split())
    edges = []
    for i in xrange(WL):
        u, v, w = map(int, raw_input().strip().split())
        u = u - 1
        v = v - 1
        edges.append((u, v, w))

    for i in xrange(WD):
        u, v, w = map(int, raw_input().strip().split())
        u = u - 1
        v = v - 1
        edges.append((v, u, -1 * w))
    
    bellman(edges, N, 0, N - 1)

if __name__ == "__main__":
    main()
