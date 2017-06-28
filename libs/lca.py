import jmatrix


def is_parent(x, y, p):
    if x == y:
        return True
    
    while y != p[y]:
        if x == p[y]:
            return True
        y = p[y]
    return False

def find(x, y, p):
    if is_parent(x, y, p):
        return x
    else:
        return find(p[x], y, p)
    

def dfs(m, node, visit, p):
    visit[node] = True
    for i in xrange(len(m[node])):
        if m[node][i] == 1:
            if visit[i] != True:
                p[i] = node
                dfs(m, i, visit, p)

def lca(m, n):
    visit = [0] * n
    lca = [ [0] * n for i in xrange(n) ]
    p = {0 : 0, 1 : 1, 2 : 2}
    for i in xrange(n):
        if visit[i] != True:
            dfs(m, i, visit, p)
    print p
    for i in xrange(n):
        for j in xrange(0, i + 1):
            lca[i][j] = lca[j][i] = find(i, j, p)
    print lca

def test_lca():
    m = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],

    ]
    print m
    lca(m, 4)

def main():
    test_lca()

if __name__ == "__main__":
    main()
