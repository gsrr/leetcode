def bfs(image, sr, sc, newColor):
    '''
    Time complexity : O(n^2)
    Result : Accept
    '''
    hist = {}
    sval = image[sr][sc]
    q = [(sr, sc)]
    while len(q) != 0:
        x, y = q.pop(0)
        if hist.get((x, y)) == True:
            continue
        hist[(x, y)] = True
        if image[x][y] == sval:
            image[x][y] = newColor
        else:
            continue
        
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx >= 0 and nx < len(image) and ny >= 0 and ny < len(image[nx]):
                q.append((nx, ny))    
    
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(image, sr, sc, newColor):
            '''
            Time Complexity : O(n^2)
            Result : Accept
            '''
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]):
                return 
            if image[sr][sc] != sval:
                return
            
            if hist.has_key((sr, sc)):
                return
            
            hist[(sr, sc)] = True
            image[sr][sc] = newColor
            dfs(image, sr + 1, sc, newColor)
            dfs(image, sr - 1, sc, newColor)
            dfs(image, sr, sc + 1, newColor)
            dfs(image, sr, sc - 1, newColor)
            
            
        #bfs(image, sr, sc, newColor)
        hist = {}
        sval = image[sr][sc] 
        dfs(image, sr, sc, newColor)
        return image
