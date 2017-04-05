
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

def tree_convert(func):
    def wrap_func(cases, cn = 1):
        treecases = []
        for case in cases:
            tmpcases = []
            for ca in case:
                root = None
                for i in ca:
                    root = tree_insert(root, i)    
                tmpcases.append(copy.deepcopy(root))
            treecases.append(copy.deepcopy(tmpcases))
        return func(treecases, cn)
    return wrap_func

def bfs(root, path):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node != None:
            path.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            path.append(None)

def dfs(node, path):
    if node == None:
        path.append(None)
        return
    dfs(node.left, path)
    path.append(node.val)
    dfs(node.right, path)
    

@tree_convert
def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print cases[cnt]
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def bstree_insert(n, root):
    if root == None:
        return TreeNode(n)

    if n < root.val:
        root.left = bstree_insert(n, root.left)
    elif n > root.val:
        root.right = bstree_insert(n, root.right)
    return root

def bstree_search(root, n):
    if root == None:
        return False

    if n > root.val:
        return bstree_search(root.right, n)
    elif n < root.val:
        return bstree_search(root.left, n)
    else:
        return True

def bstree(a):
    root = None
    for i in a:
        root = bstree_insert(i, root)
    return root

def ans(a, b):
    ret1 = []
    ret2 = []
    bfs(a, ret1)
    bfs(b, ret2)
    print ret1
    print ret2
    if len(ret1) != len(ret2):
        return False
    else:
        for p,q in zip(ret1, ret2):
            if p != q:
                return False

    return True

cases = [
    [[1,1], [1,None,1]],
]
test(cases,10)

