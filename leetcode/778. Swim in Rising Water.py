import heapq

def bfs(grid):
    maxcnt = 0
    q = []
    hist = {}
    heapq.heappush(q, (grid[0][0], (0, 0)))
    while len(q) != 0:
        step, (x, y) = heapq.heappop(q)
        if hist.has_key((x, y)):
            continue
        #print step, x, y
        maxcnt = max(maxcnt, step)
        if x == len(grid) - 1 and y == len(grid[x]) - 1:
            break
       
        hist[(x, y)] = True
        for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if nx > -1 and nx < len(grid) and ny > -1 and ny < len(grid[nx]):
                heapq.heappush(q, (grid[nx][ny], (nx, ny)))
    return maxcnt

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return bfs(grid)
