#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def dfs(t, ret):
    if t == None:
        return
    dfs(t.left, ret)
    ret.append(t.val)
    dfs(t.right, ret)

cnt = 0
def dfs1(t, ret):
    global cnt
    if t == None:
        return
    dfs1(t.left, ret)
    t.val = ret[cnt]
    cnt += 1
    dfs1(t.right, ret)

def ans(t):
    ret = []
    dfs(t, ret)
    for i in xrange(len(ret) - 2, -1, -1):
        ret[i] += ret[i + 1]
    dfs1(t, ret)
    ret2 = []
    dfs(t, ret2)
    return t

t1 = TreeNode(5)
t1.left = TreeNode(2)
t1.right = TreeNode(13)

cases = [
    [t1]
]
test(cases,1)

