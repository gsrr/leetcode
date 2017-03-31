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
            root = None
            for i in case:
                root = tree_insert(root, i)    
            treecases.append([copy.deepcopy(root)])
        return func(treecases, cn)
    return wrap_func

def bfs(root):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        print node.val
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)


#@tree_convert
def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
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
    root = bstree(a)
    b.sort()
    ret = []
    for i in xrange(len(b)):
        if ret and ret[len(ret) - 1] == b[i]:
            continue
        if bstree_search(root, b[i]):
            ret.append(b[i])
    return ret 

cases = [
    [[1,2,2,1], [2, 2]],
    [[1], [1]]
]
test(cases,10)

