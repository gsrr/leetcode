def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(x, y):
    ret = 0
    for i in xrange(31):
        b1 = (x >> i) & 1
        b2 = (y >> i) & 1
        ret += (b1 ^ b2)
    return ret

cases = [
    [1, 4]
]
test(cases,1)

