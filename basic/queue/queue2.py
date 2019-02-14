import sys
import main

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

qu = None

def insert(val):
    global qu
    if qu == None:
        qu = Node(val)
        return
    tmp = qu
    while tmp.next != None:
        tmp = tmp.next
    tmp.next = Node(val)

def remove():
    global qu
    if qu  == None:
        return

    val = qu.val
    tmp = qu
    qu = qu.next
    tmp.next = None
    return val

def get_vals(qu):
    ret = []
    tmp = qu
    while tmp != None:
        ret.append(str(tmp.val))
        tmp = tmp.next
    return ret

def ans(q):
    global qu
    qu = None
    for i in xrange(len(q)):
        func = getattr(sys.modules[__name__], q[i][0])
        if len(q[i]) == 1:
            func()
        else:
            func(*q[i][1:])
    squ = get_vals(qu)
    return ",".join(squ)

if __name__ == "__main__":
    main.main(ans)
