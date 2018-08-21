import tree

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
ret = []

def dfs(root):
    # DLR
    global ret
    if root == None:
        return

    ret.append(root.val)
    dfs(root.left)
    dfs(root.right)
    

def test_dfs_tree():
    '''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    bfs : 1,2,3,4,5,6,7
    dfs(dlr) : 1,2,4,5,3,6,7
    '''
    global ret
    arr = [1,2,3,4,5,6,7]
    print "arr:", arr
    root = tree.tree_create(arr)
    dfs(root)
    print "dfs:", ret

test_dfs_tree()
