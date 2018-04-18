from collections import deque

def bfs(target):
    hist = {}
    q = deque([(0, 1, 0)]) # (position, speed, length)
    while True:
        #print q
        pos, speed, length = q.popleft()
        if pos < 0:
            continue
        
        if hist.has_key((pos, speed)):
            continue
        
        if abs(pos) >= (target * 2):
            continue
        hist[(pos, speed)] = length
        if pos == target:
            return length
        
        for np, ns in [(speed, 2), (0, -1)]:
            npos = pos + np
            if ns == -1:
                nspeed =  -1 if speed > 0 else 1
            else:
                nspeed = speed * 2
            q.append((npos, nspeed, length + 1))
    

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        return bfs(target)
        
