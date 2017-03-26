import time
def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(a, b):
    print "(%d,%d) = (%x,%x)"%(a,b, a,b)
    MOD     = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    while b != 0:
        a, b = (a ^ b) , ((a & b) << 1) 
        a = a & MOD
        b = b & MOD
        print "(%d,%d) = (%x,%x)"%(a,b, a,b)
        #time.sleep(1)
    return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT

cases = [
    [-1, 2],
]
test(cases,10)

