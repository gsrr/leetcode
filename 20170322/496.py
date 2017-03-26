def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def find_greater(ms, i, j):
    for k in xrange(j, len(ms)):
        if ms[k] > i:
            return ms[k]
    return -1

def ans(ns, ms):
    ms_dic = {}
    for i in xrange(len(ms)):
        ms_dic[ms[i]] = i

    ret = []
    for i in ns:
        retval = find_greater(ms, i, ms_dic[i])
        ret.append(retval)
    return ret
                

cases = [
    [[4,1,2], [1,3,4,2]]
]
test(cases,1)

