hist = {}

def get_cnts(n, k, r, c):
    if k == 0:
        return 1
    global hist
    steps = [(r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1), (r + 1, c + 2), (r - 1, c + 2), (r + 1, c - 2), (r - 1, c - 2)]
    cnt = 0
    for nr, nc in steps:
        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if hist.has_key((nr, nc, k - 1)):
                cnt += hist[(nr, nc, k - 1)]
            else:
                cnt += get_cnts(n, k - 1, nr, nc)
                
    hist[(r, c, k)] = cnt
    return cnt

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        global hist
        hist = {}
        cnts = get_cnts(N, K, r, c)
        return float(cnts) / pow(8, K)
            
