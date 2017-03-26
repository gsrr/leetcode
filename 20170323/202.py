def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def _ans(n, hist):
    tmp = n
    s = 0
    while tmp != 0:
        d = tmp % 10
        s += d * d
        tmp = tmp / 10
    if s == 1:
        return True
    else:
        if s in hist:
            return False
    hist.append(s)
    return _ans(s, hist)
    

def ans(n):
    hist = []
    return _ans(n, hist)

cases = [
    [19],       
    [99],
]
#test(cases,1)
test(cases, 10)

