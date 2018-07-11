import heapq

def bfs(grid, tnum, si, sj):
    q = []
    heapq.heappush(q, (0, si, sj, 0))
    #hist = {}
    while len(q) != 0:
        cnt, x, y, knum = heapq.heappop(q)
        print x, y, cnt, knum
        if knum == tnum:
            return cnt
        
        #if hist.has_key((x, y)):
            #continue
        
        #hist[(x, y)] = True
        for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                if grid[nx][ny] == "#":
                    continue
                    
                if grid[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    dnum = 1 << (ord(grid[nx][ny].lower())  - ord('a'))
                    if knum & dnum == 0:
                        continue
                        
                ttnum = knum
                if grid[nx][ny] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    dnum = 1 << (ord(grid[nx][ny].lower())  - ord('a'))
                    if ttnum & dnum != 0:
                        continue
                    ttnum |= (1 << (ord(grid[nx][ny])  - ord('a')))

                heapq.heappush(q, (cnt + 1, nx, ny, ttnum))
    return -1            

def ans1(grid):
    #for i in xrange(len(grid)):
        #print grid[i]
    keys = 0
    si, sj = (0, 0)
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] in ['a', 'b', 'c', 'd', 'e', 'f']:
                keys |= (1 << (ord(grid[i][j])  - ord('a')))
            if grid[i][j] == '@':
                si, sj = (i, j)
    print keys
    print si, sj
    
    return bfs(grid, keys, si, sj)

ghist = {}

def bfs1(grid, s, t, kset):
    global ghist
    gkey = str(s) + str(t) + str(kset)
    if ghist.has_key(gkey):
        return ghist[gkey]
    
    x, y = s[0], s[1]
    q = [(x, y, 0)]
    hist = {}
    while len(q) != 0:
        x, y, cnt = q.pop(0)
        #print x, y, cnt
        if x == t[0] and y == t[1]:
            #print "bfs:", s, t, cnt
            ghist[gkey] = cnt
            return cnt
        
        if hist.has_key((x, y)):
            continue
        
        hist[(x, y)] = True
        for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                if grid[nx][ny] == "#":
                    continue
                    
                if grid[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    if grid[nx][ny].lower() not in kset:
                        continue
                q.append((nx, ny, cnt + 1))
    #print "bfs:", s, t, -1
    ghist[gkey] = -1
    return -1 

def recur_util(keys, grid, s, kset):
    #print keys, s, kset
    if len(keys) == len(kset):
        return 0
    
    gmin = 0x7fffffff
    for i in xrange(len(keys)):
        key = keys[i]
        if key[0] in kset:
            continue
            
        dist = bfs1(grid, s, key[1], kset)
        if dist == -1:
            continue
        kset.add(key[0])
        tmin = recur_util(keys, grid, key[1], kset)
        if tmin == -1:
            continue
        if dist + tmin < gmin:
            gmin = dist + tmin
        kset.remove(key[0])
    
    if gmin == 0x7fffffff:
        gmin = -1
    return gmin

def ans(grid):
    #for i in xrange(len(grid)):
        #print grid[i]
    
    global ghist
    ghist = {}
    
    keys = []
    si, sj = (0, 0)
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] in ['a', 'b', 'c', 'd', 'e', 'f']:
                keys.append([grid[i][j], (i, j)])
            if grid[i][j] == '@':
                si, sj = (i, j)
    #print keys
    
    gmin = 0x7fffffff
    for i in xrange(len(keys)):
        key = keys[i]
        kset = set([])
        dist = bfs1(grid, (si, sj), key[1], kset)
        if dist == -1:
            continue
        kset.add(key[0])
        tmin = recur_util(keys, grid, key[1], kset)
        if tmin == -1:
            continue
        if dist + tmin < gmin:
            gmin = dist + tmin
        kset.remove(key[0])
    if gmin == 0x7fffffff:
        gmin = -1
    return gmin
    
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        return ans(grid)
        
