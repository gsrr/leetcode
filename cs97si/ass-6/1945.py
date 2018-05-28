



def ans(n):
    hist = {}
    q = [(1, 0, 0)]
    while len(q) != 0:
        v1, v2, cnt = q.pop(0)
        if hist.has_key((v1, v2)):
            continue
        if  v1 == n or v2 == n:
            return cnt
        hist[(v1, v2)] = True
        for nv1, nv2 in [(v1 + v1, v2), (v1, v1 + v1), (v1 + v2, v2), (v1, v1 + v2), (v2 + v2, v2), (v1, v2 + v2), (v1, v1 - v2), (v1 - v2, v2), (v1, v2 - v1), (v2 - v1, v2)]:
            if nv1 > nv2:
                q.append((nv1, nv2, cnt + 1))
            else:
                q.append((nv2, nv1, cnt + 1))


n = int(input())
print (ans(n))
