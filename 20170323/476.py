import math

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(n):
    ret = 0
    tmp = n 
    cnt = 0
    while tmp/2 != 0:
        bit = tmp & 1
        ret = ret + pow(2, cnt) * (1 - bit)
        tmp = tmp >> 1
        cnt += 1

    return ret

cases = [
    [5],       
    [1],
    [4],
]
test(cases, 10)

