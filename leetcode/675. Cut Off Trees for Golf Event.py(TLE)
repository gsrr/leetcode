def convert(matrix, forest):
    nums = []
    for i in xrange(len(forest)):
        for j in xrange(len(forest[i])):
            nums.append([forest[i][j],(i, j)])
    
    nums.sort()

    cnt = 2
    for i in xrange(len(nums)):
        val = nums[i][0]
        x, y = nums[i][1]
        if val == 0 or val == 1:
            matrix[x][y] = val
        else:
            matrix[x][y] = cnt
            cnt += 1
    return cnt - 1

def bfs_find_next(tval, x, y, matrix):
    hist = {}
    q = [(x, y, 0)]
    while len(q) != 0:
        cx, cy, steps = q.pop(0)
        if hist.has_key((cx, cy)) == True:
            continue
        if matrix[cx][cy] == tval:
            return (cx, cy, steps)
        
        hist[(cx, cy)] = True
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if nx > -1 and nx < len(matrix) and ny > -1 and ny < len(matrix[nx]):
                if matrix[nx][ny] == 0:
                    continue
                q.append((nx, ny, steps + 1))
                
    return (0, 0, -1)
    
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for j in xrange(len(forest[i]))] for i in xrange(len(forest))]
        mval = convert(matrix, forest)
        if mval == 1:
            return 0
        cval = 1
        x, y = 0, 0
        cnt = 0
        print matrix
        '''
        while cval < mval:
            nx, ny, steps = bfs_find_next(cval + 1, x, y, matrix)
            if steps == -1:
                cnt = -1
                break
            cnt += steps
            cval += 1
            x, y = nx, ny
        return cnt
        '''
