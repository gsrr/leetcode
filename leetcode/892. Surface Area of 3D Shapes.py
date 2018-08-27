def get_up_low(grid):
    val = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j]!= 0:
                val += 1
    return 2 * val

def get_left_right(grid):
    val = 0
    for i in xrange(len(grid)):
        tval = grid[i][0]
        for j in xrange(1, len(grid[i])):
            if grid[i][j] - grid[i][j - 1] > 0:
                tval += (grid[i][j] - grid[i][j - 1])
        val += tval
    return 2 * val

def get_fb(grid):
    tgrid = [list(x) for x in zip(*grid)]
    return get_left_right(tgrid)
    
def ans(grid):
    ul = get_up_low(grid)
    lr = get_left_right(grid)
    fb = get_fb(grid)
    return ul + lr + fb

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return ans(grid)    
