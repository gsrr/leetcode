import heapq

def bfs(grid):
    hist = {}
    q = [(grid[0][0], 0, 0)]
    while len(q) != 0:
        val, x, y = heapq.heappop(q)
        if x == (len(grid) - 1) and y == (len(grid[x]) - 1):
            return val
        if hist.has_key((x, y)):
            continue
        
        hist[(x, y)] = True
        for nx, ny in [(x, y + 1), (x + 1, y)]:
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                heapq.heappush(q, (grid[nx][ny] + val, nx, ny))
    
    
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return bfs(grid)
