def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def getrow(s, dic):
    for key in dic.keys():
        if s[0] in key:
            return dic[key]
    return 0

def ans(n):
    ret = []
    dic = {"QWERTYUIOP" : 1, "ASDFGHJKL" : 2, "ZXCVBNM" : 3}
    for s in n:
        tmp = s.upper()
        row = getrow(tmp, dic)
        for c in tmp[1:]:
            for key in dic.keys():
                if c in key:
                    if row != dic[key]:
                        row = 0
                        continue
        if row != 0:
            ret.append(s)
    return ret

cases = [
    [["Hello", "Alaska", "Dad", "Peace"]],       
    [["adsdf","sfd"]],
]
#test(cases,1)
test(cases, 10)

