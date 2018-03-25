def trans(grid):
    for i in xrange(len(grid)):
        for j in xrange(i + 1, len(grid[i])):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

def ans1(grid):
    row_arr = [0] * len(grid)
    col_arr = [0] * len(grid[0])
    for i in xrange(len(grid)):
        row_arr[i] = max(grid[i])

    trans(grid)
    for i in xrange(len(grid)):
        col_arr[i] = max(grid[i])
    
    cnt = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            cnt += (min(row_arr[j], col_arr[i]) - grid[i][j])
    
    return cnt

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return ans1(grid)
        
