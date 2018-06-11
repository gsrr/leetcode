import collections

def ans(n, arr):
    graph = [ [0] * n for _ in xrange(n) ]
    for i in xrange(len(arr)):
        tarr = arr[i]
        u = i
        for j in xrange(1, len(tarr), 2):
            v = tarr[j] - 1
            w = tarr[j + 1]
            graph[u][v] = w
    #print graph
    
    dp = [ [float("inf")] * n for _ in xrange(n) ]
    for i in xrange(len(graph)):
        dp[i][i] = 0
        for j in xrange(len(graph[i])):
            if graph[i][j] != 0:
                dp[i][j] = graph[i][j]
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    #print dp
    gmin = float("inf")
    gi = 0
    for i in xrange(len(dp)):
        lmax = max(dp[i])
        if gmin > lmax:
            gmin = lmax
            gi = i
    print gi + 1, gmin

def main():
    while True:
        n = int(raw_input())
        if n == 0:
            break
        arr = []
        for i in xrange(n):
            tarr = list(map(int, raw_input().strip().split()))
            arr.append(tarr)
        ans(n, arr)

if __name__ == "__main__":
    main()
