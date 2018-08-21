import tree

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

def bfs(root):
    ret = []
    q = [root]
    for item in q:
        if item != None:
            ret.append(item.val)
            q.append(item.left)
            q.append(item.right)
    return ret

def test_bfs_tree():
    '''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    bfs : 1,2,3,4,5,6,7
    dfs(dlr) : 1,2,4,5,3,6,7
    '''
    arr = [1,2,3,4,5,6,7]
    print "arr:", arr
    root = tree.tree_create(arr)
    print "bfs:", bfs(root)

test_bfs_tree()
