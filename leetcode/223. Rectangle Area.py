def ans(x1, y1, x2, y2, x3, y3, x4, y4):
    overlap = -1
    if x3 >= x2 or x1 >= x4:
        overlap = 0
    if y3 >= y2 or y1 >= y4:
        overlap = 0
    
    if overlap == -1:
        xarr = [x1, x2, x3, x4]
        yarr = [y1, y2, y3, y4]
        xarr.sort()
        yarr.sort()
        overlap = (xarr[2] - xarr[1]) * (yarr[2] - yarr[1])
    total = (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3)
    
    return total - overlap

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return ans(A, B, C, D, E, F, G, H)
