import sys
import main

# Double linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

st = None

def push(val):
    global st
    if st == None:
        st = Node(val)
        return
    
    pre = st
    st.next = Node(val)
    st = st.next
    st.pre = pre

def pop():
    global st
    if st == None:
        return
    
    val = st.val
    st = st.pre
    if st != None:
        st.next = None

def get_nodes(st):
    ret = []
    while st != None:
        ret.append(str(st.val))
        st = st.pre
    return ret[::-1]

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
