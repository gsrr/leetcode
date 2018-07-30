ist = {}
def recur_util(piles, turn):
    global ghist
    key = "%d:%s"%(turn, str(piles))
    if ghist.has_key(key):
        return ghist[key]
    
    
    if len(piles) == 1:
        return piles[0]

    mval = 0
    if turn % 2 == 1:
        mval = max(recur_util(piles[1:], 1 - turn), recur_util(piles[:-1], 1 - turn))
    else:
        mval = max(piles[0] + recur_util(piles[1:], 1 - turn), piles[-1] + recur_util(piles[:-1], 1 - turn))
    ghist[key] = mval
    return mval

def ans(piles):
    global ghist
    ghist = {}
    sval = sum(piles)
    
    aval = max(piles[0] + recur_util(piles[1:], 1), piles[-1] + recur_util(piles[:-1], 1))
    return aval > (sval // 2)

def minMax(piles, s, e, turn):
    global ghist
    
    if s == e:
        return 0
    
    key = (s, e)
    if ghist.has_key(key):
        return ghist[key]
    
    rval = 0
    if turn == 0:
        rval = max(piles[s] + minMax(piles, s + 1, e, 1 - turn), piles[e - 1] + minMax(piles, s, e - 1, 1 - turn))
    else:
        rval = max(minMax(piles, s + 1, e, 1 - turn), minMax(piles, s, e - 1, 1 - turn))
    ghist[key] = rval
    return ghist[key]
    
def ans1(piles):
    global ghist
    ghist = {}
    
    sval = sum(piles)
    s = 0
    e = len(piles)
    aval = max(piles[0] + minMax(piles, s + 1, e, 1), piles[-1] + minMax(piles, s, e - 1, 1))
    return aval > (sval // 2)

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return ans1(piles)
        
