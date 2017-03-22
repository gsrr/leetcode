def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

import time

def bfs(matrix, i, j, hist, dist):
    path = []
    q = []
    path.append((i, j))
    q.append((i, j, dist))
    min_val = 9999
    #print "start:", i, j
    while len(q)!= 0:
        #time.sleep(1)
        x, y, d = q.pop(0)
        #print x, y , d, matrix[x][y], q
        if d >= min_val:
            continue
        if hist.has_key((x, y)):
            if hist[(x, y)] + d < min_val:
                min_val = hist[(x, y)] + d
                continue

        if matrix[x][y] == 0:
            if 0 + d < min_val:
                min_val = 0 + d
            continue

        if d < min_val - 1:
            if y + 1 < len(matrix[x]):
                    if (x, y + 1) not in path:
                        path.append((x, y + 1))
                        q.append((x, y + 1, d + 1))
            if y - 1 > -1:
                    if (x, y - 1) not in path:
                        path.append((x, y - 1))
                        q.append((x, y - 1, d + 1))
            if x - 1 > -1:
                    if (x - 1, y) not in path:
                        path.append((x - 1, y))
                        q.append((x - 1, y, d + 1))
            if x + 1 < len(matrix):
                    if (x + 1, y) not in path:
                        path.append((x + 1, y))
                        q.append((x + 1, y, d + 1))
    #print "end:", i, j, min_val
    return min_val

def ans(n):
    hist = {}
    for i in xrange(len(n)):
        for j in xrange(len(n[i])):
            if n[i][j] != 0:
                n[i][j] = bfs(n, i, j, hist, 0)
                hist[(i, j)] = n[i][j]
        print n[i]
    return n

cases = [
    [
        [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]
    ]


]
test(cases,1)

