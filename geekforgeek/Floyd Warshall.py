#code

def floyd_warshall(graph, n):
    dp = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = graph[i][j]
    
    for i in range(n):
        dp[i][i] = 0
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for i in range(n):
        for j in range(n):
            print (dp[i][j], end = " ")
    print ("")
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    graph = []
    for i in range(n):
        graph.append(arr[n * i: n * (i + 1)])
    floyd_warshall(graph, n)
