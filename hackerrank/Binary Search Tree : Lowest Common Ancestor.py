"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def find_parent(parent, u, v):
    if v == -1:
        return False
    if parent[v] == u:
        return True
    return find_parent(parent, u, parent[v])

def find(parent, u, v):
    if u== v:
        return u
    else:
        if find_parent(parent, u, v) == True:
            return u
        else:
            return find(parent, parent[u], v)

mapp = {}

def dfs(parent, root, p = -1):
    global mapp
    mapp[root.data] = root
    parent[root.data] = p
    if root.left != None:
        dfs(parent, root.left, root.data)
    if root.right != None:
        dfs(parent, root.right, root.data)

def lca(root , v1 , v2):
    global mapp
    #Enter your code here
    parent = {}
    dfs(parent, root)
    #print parent
    val = find(parent, v1, v2)
    return mapp[val]
