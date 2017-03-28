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

@tree_convert
def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(root):
    if root == None:
        return 0
    lh = 1
    rh = 1
    if root.left != None:
        lh = 1 + ans(root.left)
    if root.right != None:
        rh = 1 + ans(root.right)
    return max(lh, rh)

cases = [
    [1, 4, 5, 7, 8]
]
test(cases,1)
