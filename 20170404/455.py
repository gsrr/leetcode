
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
            ret.append(cnt)
        cnt += 1
    return ret

def ans(a,b):
    a.sort()
    b.sort()
    cnt = 0
    s = 0
    for i in xrange(len(b)):
        for j in xrange(s, len(a)):
            if b[i] < a[j]:
                break
            if b[i] >= a[j] and a[j] != 0:
                cnt += 1
                a[j] = 0
                s = j
                break
    return cnt

cases = [
    [[1,2,3],[1,1]],
]
test(cases,1)

