import sys

st = []

def push(val):
    global st
    st.append(val)

def pop():
    global st
    st.pop()

def ans(q):
    global st
    st = []
    for i in xrange(len(q)):
        func = getattr(sys.modules[__name__], q[i][0])
        if len(q[i]) == 1:
            func()
        else:
            func(*q[i][1:])
    sst = [ str(x) for x in st]
    return ",".join(sst)

def read_file(fname):
    with open(fname, "r") as fr:
        lines = fr.readlines()
        j = 0
        for i in xrange(0, len(lines), 2):
            q = lines[i].strip()
            a = lines[i + 1].strip()
            ret = ans(eval(q))
            print "Case %d: %s == %s"%(j + 1, ret, a), ret == a
            j += 1

def main():
    name = __file__.strip(".py")
    cname = name + ".case"
    read_file(cname)

if __name__ == "__main__":
    main()
