def bfs1(grid, pos, hist):
    q = []
    q.append(pos)
    thist = {}
    cnt = 0
    while len(q) != 0:
        x, y = q.pop(0)
        if thist.has_key((x, y)):
            continue
        thist[(x, y)] = True
        cnt += 1
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                if grid[nx][ny] == 1:
                    q.append([nx, ny])
    return cnt

def ans1(grid):
    '''
    Result : Time limit exceed
    '''
    zeros = []
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] == 0:
                zeros.append([i, j])
    if len(zeros) == 0:
        return len(grid) * len(grid[0])
    hist = {}
    cnt = 0
    
    for i in xrange(len(zeros)):
        grid[zeros[i][0]][zeros[i][1]] = 1
        tcnt = bfs(grid, zeros[i], hist)
        hist[tuple(zeros[i])] = tcnt
        if tcnt > cnt:
            cnt = tcnt
        grid[zeros[i][0]][zeros[i][1]] = 0
    return cnt

def bfs(grid, hist):
    thist = {}
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            if grid[i][j] == 0:
                hist[(i, j)] = (i, j, 0)
                continue
            else:  
                base = (i, j)
                if thist.has_key((i, j)):
                    hist[base] = hist[thist[base]]
                    continue
                q = [(i, j)]
                cnt = 0
                while len(q) != 0:
                    x, y = q.pop(0)
                    if thist.has_key((x, y)):
                        continue
                    thist[(x, y)] = (i, j)
                    cnt += 1
                    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                            if grid[nx][ny] == 1:
                                q.append([nx, ny])
                hist[base] = (i, j, cnt)

def ans(grid):
    '''
    Result : 
    '''
    zeros = []
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] == 0:
                zeros.append([i, j])
    if len(zeros) == 0:
        return len(grid) * len(grid[0])
    
    hist = {}
    bfs(grid, hist)
    cnt = 0
    for i in xrange(len(zeros)):
        x, y = zeros[i]
        tcnt = 1
        thist = {}
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                tx, ty, kcnt = hist[(nx, ny)]
                if thist.has_key((tx,ty)):
                    continue
                tcnt += kcnt
                thist[(tx, ty)] = True
        print
        if tcnt > cnt:
            cnt = tcnt
    return cnt

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return ans(grid)
