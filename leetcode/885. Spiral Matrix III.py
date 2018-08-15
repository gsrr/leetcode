                     
def ans(R, C, r0, c0):
    ret = []
    total = R * C
    matrix = [ [0] * (C + 2) for _ in xrange(R + 2) ]
    q = [(r0 + 1, c0 + 1, "start")]
    while len(ret) != (R * C):
        r, c, direct = q.pop(0)
        if r != (R + 1) and c != (C + 1) and r != 0 and c != 0:
            matrix[r][c] = 1
            ret.append([r - 1, c - 1])
            
        if direct == "start":
            nr = r
            nc = c + 1
            q.append((nr, nc, "east"))
        elif direct == "east":
            if matrix[r + 1][c] == 0:
                q.append((r + 1, c, "south"))
            else:
                q.append((r, c + 1, "east"))
        elif direct == "south":
            if matrix[r][c - 1] == 0:
                q.append((r, c - 1, "west"))
            else:
                q.append((r + 1, c, "south"))
        elif direct == "west":
            if matrix[r - 1][c] == 0:
                q.append((r - 1, c, "north"))
            else:
                q.append((r, c - 1, "west"))
        elif direct == "north":
            if matrix[r][c + 1] == 0:
                q.append((r, c + 1, "east"))
            else:
                q.append((r - 1, c, "north"))
    return ret
    
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        return ans(R, C, r0, c0)
