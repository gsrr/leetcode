def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def factor(n):
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            ret.append([cnt, n/cnt])
            ret.append([n/cnt, cnt])
        cnt += 1
    return ret

def isillegal(e):
    if e[0] < e[1]:
        return True
    return False

def ismin(m, e):
    if (e[0] - e[1]) < (m[0] - m[1]):
        return True
    return False

def ans(a):
    ret = [0x7fffffff, 0]
    edges = factor(a)
    print edges
    for e in edges:
        if isillegal(e):
            continue   
        if ismin(ret, e):
            ret = e
    return ret

cases = [
    [4],
    [9999998],
]
test(cases,10)

