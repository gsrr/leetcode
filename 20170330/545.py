import copy

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_insert(root, i):
    if root == None:
        return TreeNode(i)

    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node.left == None:
            node.left = TreeNode(i)
            break
        else:
            q.append(node.left)
        if node.right == None:
            node.right = TreeNode(i)
            break
        else:
            q.append(node.right)

    return root

def remove_none(root):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node.left != None:
            if node.left.val == None:
                node.left = None
            else:
                q.append(node.left)
        if node.right != None:
            if node.right.val == None:
                node.right = None
            else:
                q.append(node.right)
    return root

def tree_convert(func):
    def wrap_func(cases, cn = 1):
        treecases = []
        for case in cases:
            root = None
            for i in case:
                root = tree_insert(root, i)    
            remove_none(root)
            treecases.append([copy.deepcopy(root)])
        return func(treecases, cn)
    return wrap_func

def bfs(root):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        print node.val, node.left, node.right
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)


@tree_convert
def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def dlr(node, ret, rootval):
    ret.append( node.val)
    if node.left == None and node.right == None:
        return

    if node.left != None:
        dlr(node.left, ret, False)
    else:
        if rootval == False:
            dlr(node.right, ret, False)

def find_leaf(node, ret):
    if node.left == None and node.right == None:
        ret.append( node.val)
    if node.left != None:
        find_leaf(node.left, ret)
    if node.right != None:
        find_leaf(node.right, ret)

def drl(node, ret, rootval):
    ret.append(node.val)
    if node.left == None and node.right == None:
        return

    if node.right != None:
        drl(node.right, ret, False)
    else:
        if rootval == False:
            drl(node.left, ret, False)

def ans(root):
    if root == None:
        return []
    ret = []
    ret1 = []
    ret2 = []
    ret3 = []
    dlr(root, ret1, True)
    find_leaf(root, ret2)
    drl(root, ret3, True)
    print ret1, ret2, ret3[::-1]
    if len(ret1) == 1 and len(ret2) == 1 and len(ret3) == 1:
        return ret1
    ret = ret1 + ret2 + ret3[::-1]
    retf = ret1
    if ret1[-1] == ret2[0]:
        if len(ret1) != 1 and len(ret2) != 1:
            retf += ret2[1:]
        else:
            retf += ret2
    else:
        retf += ret2
    if ret2[-1] == ret3[::-1][0]:
        retf += ret3[::-1][1:-1]
    else:
        retf += ret3[::-1][:-1]
    return retf

cases = [
    [1,None, 2, None, None, 3,4],
]
test(cases,10)

