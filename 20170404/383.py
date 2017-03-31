
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

def ans(a, b):
    dic_char = {}
    for i in b:
        if dic_char.has_key(i) == False:
            dic_char[i] = 0
        dic_char[i] += 1
    for i in a:
        if dic_char.has_key(i) == False:
            return False
        dic_char[i] -= 1
        if dic_char[i] == -1:
            return False
    return True


cases = [
    ["aa", "aab"],
]
test(cases,1)

