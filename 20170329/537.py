def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def isdigit(c):
    try:
        int(c)
        return True
    except:
        return False

def ans(a, b):
    def cvt(x):
        a,b = x.split('+')
        b = b[:-1]
        return int(a) + int(b)*1j
    print a, b
    a,b = cvt(a), cvt(b)
    print a, b
    c = a*b
    return "{}+{}i".format(int(c.real), int(c.imag))

cases = [
    ["1+1i", "1+1i"],
    ["1+1i", "2+1i"],
    ["1+-1i", "2+-1i"],
    ["1+-1i", "1+-1i"],
    ["78+-76i", "-86+72i"],
    ["20+22i", "-18+-10i"]
]
test(cases,10)

