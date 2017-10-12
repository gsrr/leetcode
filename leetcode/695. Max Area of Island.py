def bfs(grid, q, hist):
    max_area = 0
    while len(q) != 0:
        x, y = q.pop(0)
        if hist.has_key((x, y)):
            continue
        if grid[x][y] == 0:
            continue
        hist[(x, y)] = True
        max_area += 1
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                q.append((i, j))
    return max_area
    
    
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        hist = {}
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    q = [(i, j)]
                    max_area = max(bfs(grid, q, hist), max_area)
        return max_area        
