ns(carr, oarr):
    oset = set([])
    for o in oarr:
        oset.add(str(o))
    
    #print oset
    pos = [0, 0]
    direct = [0, 1]
    gmax = 0
    for c in carr:
        #print c, pos, direct
        if c == -1:
            if direct ==  [0, 1]:
                direct = [1, 0]
            elif direct ==  [1, 0]:
                direct = [0, -1]
            elif direct == [0, -1]:
                direct = [-1, 0]
            elif direct == [-1, 0]:
                direct = [0, 1]
            continue
        
        if c == -2:
            if direct ==  [0, 1]:
                direct = [-1, 0]
            elif direct ==  [-1, 0]:
                direct = [0, -1]
            elif direct == [0, -1]:
                direct = [1, 0]
            elif direct == [1, 0]:
                direct = [0, 1]
            continue
        
        
        for d in xrange(c):
            x = pos[0] + direct[0]
            y = pos[1] + direct[1]
            if str([x, y]) in oset:
                #print "in oset:%s"%str([x, y]) 
                pass
            else:
                pos[0] = x
                pos[1] = y
            tmax = pos[0] * pos[0] + pos[1] * pos[1]
            gmax = max(gmax, tmax) 
    #print pos,direct
    return gmax
        
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        return ans(commands, obstacles)
        
