

def bfs(matrix, x, y, visited):
    cnt = 0
    q = [(x, y)]
    while len(q) != 0:
        u, v = q.pop(0)
        if visited[u][v] == 1:
            continue
        visited[u][v] = 1
        cnt += 1
        val = matrix[u][v]
        for d in [1, 2, 4, 8]:
            if val & d != 0:
                continue
            if d == 1:
                q.append((u, v - 1))
            elif d == 2:
                q.append((u - 1, v))
            elif d == 4:
                q.append((u, v + 1))
            elif d == 8:
                q.append((u + 1, v))
    return cnt

def ans(matrix, n, m):
    #print (matrix)
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    max_val = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] != 0:
                continue
            max_val = max(max_val, bfs(matrix, i, j, visited))
            cnt += 1
    return (cnt, max_val)

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    arr = list(map(int, input().split()))
    matrix.append(list(arr))

print (ans(matrix, n, m))
