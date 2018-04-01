import sys
sys.setrecursionlimit(100000)

options = [(100, 0), (75, 25), (50, 50), (25, 75)]
hist = {}

def soup_util(soup):
    global options
    global hist
    if hist.has_key(soup):
        return hist[soup]
    
    if soup[0] <= 0 and soup[1] <= 0:
        return 0.5 / 4
    
    if soup[0] <= 0:
        return 1.0 / 4
    
    if soup[1] <= 0:
        return 0.0
    
    prob = 0
    for opt in options:
        prob += soup_util((soup[0] - opt[0], soup[1] - opt[1]))
    
    hist[soup] = prob / 4.0
    return float(prob) / 4.0

def soup_util2(soup, hist):
    global options
    if hist.has_key(soup):
        return hist[soup]
    
    if soup[0] <= 0 and soup[1] <= 0:
        return 0.5
    
    if soup[0] <= 0:
        return 1.0
    
    if soup[1] <= 0:
        return 0.0
    
    prob = 0
    for opt in options:
        prob += soup_util2((soup[0] - opt[0], soup[1] - opt[1]), hist)
    
    hist[soup] = prob
    return float(prob)

def ans1(N):
    '''
    Result :Time exceed
    
    '''
    global options
    if N == 0:
        return 0.5
    if N >5000:
        return 1
    prob = 0
    init = (N, N)
    #hist = {}
    for opt in options:
        prob += soup_util((N - opt[0], N - opt[1]))
    return prob

class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        return ans1(N)
        #for i in xrange(100, 200):
            #print i, ans1(i)
        
