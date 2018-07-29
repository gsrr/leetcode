
global sval

def recur_util(piles, turn, aval):
    global sval
    if len(piles) == 1:
        return piles[0]

    if aval > (sval // 2):
        return True
    
    mval = 0
    if turn % 2 == 1:
        if recur_util(piles[1:], 1 - turn, aval):
            return True
        if recur_util(piles[:-1], 1 - turn, aval):
            return True
    else:
        if recur_util(piles[1:], 1 - turn, piles[0] + aval):
            return True
        if recur_util(piles[:-1], 1 - turn, piles[-1] + aval):
            return True
    return False

def ans(piles):
    global sval
    sval = sum(piles)
    
    if recur_util(piles[1:], 1, piles[0]):
        return True
    if recur_util(piles[:-1], 1, piles[-1]):
        return True
    return False

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return ans(piles)
        
