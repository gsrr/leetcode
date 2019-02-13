import sys
import main

# Single linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

st = None

def push(val):
    global st
    if st == None:
        st = Node(val)
        return
    
    tmp = st
    while tmp.next != None:
        tmp = tmp.next

    tmp.next = Node(val)

def pop():
    global st
    if st == None:
        return
    
    if st.next == None:
        val = st.val
        st = None
        return val

    pre = None
    tmp = st
    while tmp.next != None:
        pre = tmp
        tmp = tmp.next
    pre.next = None
    return tmp.val

def get_nodes(st):
    ret = []
    tmp = st
    while tmp != None:
        ret.append(str(tmp.val))
        tmp = tmp.next
    return ret

def ans(q):
    global st
    st = None
    for i in xrange(len(q)):
        func = getattr(sys.modules[__name__], q[i][0])
        if len(q[i]) == 1:
            func()
        else:
            func(*q[i][1:])
    sst = get_nodes(st)
    return ",".join(sst)

if __name__ == "__main__":
    main.main(ans)
