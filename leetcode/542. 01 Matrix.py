
def bfs(matrix, i, j, hist):
    q = [(i, j, 0)]
    hist[(i, j)] = 0
    while len(q) != 0:
        x, y, dist = q.pop(0)
        if dist > 1:
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[nx]):
                    if matrix[nx][ny] == 0:
                        hist[(x, y)] = 1
                        dist = 1
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[nx]):
                if matrix[nx][ny] == 0:
                    continue
                if hist.has_key((nx, ny)):
                    if dist + 1 < hist[(nx, ny)]:
                        q.append((nx, ny, dist + 1))
                        hist[(nx, ny)] = dist + 1
                else:
                    q.append((nx, ny, dist + 1))
                    hist[(nx, ny)] = dist + 1
    return matrix



class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        hist = {}
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    bfs(matrix, i, j, hist)
        for k in hist.keys():
            matrix[k[0]][k[1]] = hist[k]
        return matrix
