

import copy

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_insert(root, i, cnt):
    none_cnt = cnt
    if root == None:
        return TreeNode(i)

    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node.left == None:
            if none_cnt != 0:
                none_cnt -= 1
            else:
                node.left = TreeNode(i)
                break
        else:
            q.append(node.left)
        if node.right == None:
            if none_cnt != 0:
                none_cnt -= 1
            else:
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
                none_cnt = 0
                for i in ca:
                    if i == None:
                        none_cnt += 1
                        continue
                    root = tree_insert(root, i, none_cnt)    
                tmpcases.append(copy.deepcopy(root))
            treecases.append(copy.deepcopy(tmpcases))
        return func(treecases, cn)
    return wrap_func

def bfs(root):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node == None:
            print None
            continue
        print node.val
        q.append(node.left)
        q.append(node.right)


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


ret = 0
def _ans(node, s, path):
    global ret
    if node == None:
        return

    tmp = node.val
    for i in path[::-1]:
        tmp += i
        if tmp == s:
            ret += 1
    
    path.append(node.val)
    _ans(node.left, s, path)
    _ans(node.right, s, path)
    path.pop()

def ans(a, s):
    path = []
    _ans(a, s.val, path)
    return ret
    

cases = [
    [[10,5,-3,3,2,None,11,3,-2,None,1], [8]],
]
test(cases,10)

