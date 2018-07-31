ghist = {}
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

def minMax1(piles, s, e, turn):
    global ghist
    
    if s == e:
        return 0
    
    key = (s, e)
    if ghist.has_key(key):
        return ghist[key]
    
    rval = 0
    if turn == 0:
        rval = max(piles[s] + minMax1(piles, s + 1, e, 1 - turn), piles[e - 1] + minMax1(piles, s, e - 1, 1 - turn))
    else:
        rval = max(minMax1(piles, s + 1, e, 1 - turn), minMax1(piles, s, e - 1, 1 - turn))
    ghist[key] = rval
    return ghist[key]
    
def ans1(piles):
    global ghist
    ghist = {}
    
    sval = sum(piles)
    s = 0
    e = len(piles)
    aval = max(piles[0] + minMax1(piles, s + 1, e, 1), piles[-1] + minMax1(piles, s, e - 1, 1))
    return aval > (sval // 2)

def minMax2(piles, s, e, turn):
    global ghist
    
    if s == e:
        return 0
    
    key = (s, e, turn)
    if ghist.has_key(key):
        return ghist[key]
    
    rval = 0
    if turn == 0:
        rval = max(piles[s] + minMax2(piles, s + 1, e, 1 - turn), piles[e - 1] + minMax2(piles, s, e - 1, 1 - turn))
    else:
        rval = max(minMax2(piles, s + 1, e, 1 - turn), minMax2(piles, s, e - 1, 1 - turn))
    ghist[key] = rval
    return ghist[key]
    
def ans2(piles):
    global ghist
    ghist = {}
    
    sval = sum(piles)
    s = 0
    e = len(piles)
    aval = max(piles[0] + minMax2(piles, s + 1, e, 1), piles[-1] + minMax2(piles, s, e - 1, 1))
    return aval > (sval // 2)

def minMax3(piles, s, e, turn):
    global ghist
    
    if s == e:
        return 0
    
    key = (s, e, turn)
    if ghist.has_key(key):
        return ghist[key]
    
    rval = 0
    if turn == 0:
        rval = max(piles[s] + minMax3(piles, s + 1, e, 1 - turn), piles[e - 1] + minMax3(piles, s, e - 1, 1 - turn))
    else:
        rval = min(-piles[s] + minMax3(piles, s + 1, e, 1 - turn), -piles[e - 1] + minMax3(piles, s, e - 1, 1 - turn))
    ghist[key] = rval
    return ghist[key]
    
def ans3(piles):
    global ghist
    ghist = {}
    
    sval = sum(piles)
    s = 0
    e = len(piles)
    aval = max(piles[0] + minMax3(piles, s + 1, e, 1), piles[-1] + minMax3(piles, s, e - 1, 1))
    return aval > 0

def ans4(piles):
    # piles.length is even.
    
    dp = [[0] * (len(piles) + 1) for _ in xrange(len(piles) + 1)]
    
    for i in xrange(len(dp)):
        dp[i][i] = 0
        
    for k in xrange(1, len(dp)):
        for i in xrange(len(dp) - k):
            #print i, i + k
            if k % 2 == 0: # A turn
                dp[i][i + k] = max( piles[i] + dp[i + 1][i + k], piles[i + k - 1] + dp[i][i + k - 1] )
            else:
                dp[i][i + k] = min( -piles[i] + dp[i + 1][i + k], -piles[i + k - 1] + dp[i][i + k - 1] )
    
    #print dp
    return dp[0][-1] > 0
                
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return ans4(piles)
        
