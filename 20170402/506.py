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

G = "Gold Medal"
S = "Silver Medal"
B = "Bronze Medal"

def ans(a):
    dic = {}
    for i in xrange(len(a)):
        dic[a[i]] = i
    rank = dic.keys()[::-1]
    rank.sort(reverse=True)
    print rank
    cnt = 1
    for r in rank:
        if cnt == 1:
            a[dic[r]] = "Gold Medal"
        elif cnt == 2:
            a[dic[r]] = "Silver Medal"
        elif cnt == 3:
            a[dic[r]] = "Bronze Medal"
        else:
            a[dic[r]] = str(cnt)
        cnt += 1 
    return a

cases = [
    [[5, 4, 3, 2, 1]],
]
test(cases,1)

