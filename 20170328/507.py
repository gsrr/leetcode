import math

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans_(a):
    for a in xrange(3, 100000000):
        if a % 10 != 6 and a % 10 != 8:
            continue
        n = 0
        if a % 2 != 0:
            #return False
            continue
        
        n = 1
        for i in xrange(2, a/2 + 1):
            if a % i == 0:
                n = n + i   
            
        if n == a:
            print a
            #return True
    return False

def ans(a):
    if a < 0 :
        return False

    if a % 10 != 6 and a % 10 != 8:
        return False
    n = 0
    if a % 2 != 0:
        return False
    
    n = 1
    for i in xrange(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            print i
            n = n + i   
            n = n + a/i
        
    if n == a:
        return True
    return False


cases = [
    [6],
    [28],
    [-954],
]
test(cases,10)

