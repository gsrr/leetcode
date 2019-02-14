import sys
import main

qu = []

def insert(val):
    global qu
    qu.append(val)

def remove():
    global qu
    if len(qu) == 0:
        return

    qu.pop(0)

def ans(q):
    global qu
    qu = []
    for i in xrange(len(q)):
        func = getattr(sys.modules[__name__], q[i][0])
        if len(q[i]) == 1:
            func()
        else:
            func(*q[i][1:])
    squ = [ str(x) for x in qu]
    return ",".join(squ)

if __name__ == "__main__":
    main.main(ans)
