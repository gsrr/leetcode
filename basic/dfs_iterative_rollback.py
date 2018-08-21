import tree

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
    
ret = []

def dfs(root, path):
    global  ret
    path.append(str(root.val))
    if root.left == None and root.right == None:
        ret.append(" -> ".join(path))
    else:
        if root.left != None:
            dfs(root.left, path)
        if root.right != None:
            dfs(root.right, path)
    path.pop()

def dfs_iterative_rollback(root):
    # DLR
    ret = []
    st = [(0, root, [])] # (node, sval)
    while len(st) != 0:
        t, node, path = st.pop()
        if t == 0:
            path.append(str(node.val))
            if node.left == None and node.right == None:
                ret.append(" -> ".join(path))
            else: 
                if node.right != None:
                    st.append((1, node.right, path))
                    st.append((0, node.right, path))
                if node.left != None:
                    st.append((1, node.left, path))
                    st.append((0, node.left, path))
        else:
            path.pop()
    return ret

def test_dfs_iterative_tree():
    '''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    all path from root to leaf : 
    [1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]
    '''
    global ret
    arr = [1,2,3,4,5,6,7]
    print "arr:", arr
    root = tree.tree_create(arr)
    path = []
    dfs(root, path)
    print "dfs:", ret
    print "dfs_iterative_rollback:", dfs_iterative_rollback(root)

test_dfs_iterative_tree()
