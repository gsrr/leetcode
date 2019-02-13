def read_file(fname, ans):
    with open(fname, "r") as fr:
        lines = fr.readlines()
        j = 0
        for i in xrange(0, len(lines), 2):
            q = lines[i].strip()
            a = lines[i + 1].strip()
            ret = ans(eval(q))
            print "Case %d: %s == %s"%(j + 1, ret, a), ret == a
            j += 1

def main(ans):
    read_file("cases", ans)
