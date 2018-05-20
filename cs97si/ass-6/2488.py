import string

ret = "impossible"

def recur_util1(n, m, path):
    global ret
    if len(path) == n * m:
        ret = ""
        for p in path:
            ret += "%s%d"%(string.ascii_uppercase[p[1]], p[0] + 1)
        return True

    x, y = path[-1]
    for nx, ny in [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2)]:
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if (nx, ny) in path:
                continue
            path.append((nx, ny))
            rret = recur_util1(n, m, path)
            path.pop()
            if rret == True:
                return True
    return False

def ans1(n, m):
    total = n * m
    path = [(0, 0)]
    recur_util1(n, m, path)


direct = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

def recur_util(path, x, y):
    global n, m, ret
    if len(path) == n * m:
        ret = ""
        for p in path:
            ret += "%s%d"%(string.ascii_uppercase[p[1]], p[0] + 1)
        return True

    for d in direct:
        nx = x + d[0]
        ny = y + d[1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
           if (nx, ny) in path:
               continue
           path.append((nx, ny))
           if recur_util(path, nx, ny) == True:
               return True
           path.pop()
    return False

def ans():
    global n, m
    path = [(0, 0)]
    recur_util(path, 0, 0)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    ret = "impossible"
    ans()
    #ans1(n, m)
    print ("Scenario #%d:"%(i + 1))
    print (ret)
    print ("")
