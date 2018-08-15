def up(grid):
    cnt = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] != 0:
                cnt += 1
    return cnt

def row(grid):
    cnt = 0
    for i in xrange(len(grid)):
        cnt += max(grid[i])
    return cnt

def col(grid):
    cnt = 0
    for c in zip(*grid):
        cnt += max(c)
    return cnt

def ans(grid):
    return up(grid) + row(grid) + col(grid)

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return ans(grid)
        
