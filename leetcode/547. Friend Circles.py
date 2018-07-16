
def bfs(matrix, group, i):
    q = [i]
    while len(q) != 0:
        u = q.pop(0)
        if group[u] != 0:
            continue
        group[u] = 1
        for v in xrange(len(matrix[u])):
            if matrix[u][v] == 1:
                q.append(v)

def ans(matrix):
    group = [0] * len(matrix)
    cnt = 0
    for i in xrange(len(matrix)):
        if group[i] != 0:
            continue
        bfs(matrix, group, i)
        cnt += 1
    return cnt

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return ans(M)
