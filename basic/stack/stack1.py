import sys
import main

st = []

def push(val):
    global st
    st.append(val)

def pop():
    global st
    if len(st) == 0:
        return

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

if __name__ == "__main__":
    main.main(ans)
