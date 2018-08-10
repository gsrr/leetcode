import itertools

def ans(G, P, garr, parr):
    '''
    Result : Time exceed
    Time Complexity : O(2^n)
    Space Complexity : O(n)
    '''
    arr = range(len(garr))
    #print arr
    cnt = 0
    for i in xrange(1, len(arr) + 1):
        comb = itertools.combinations(arr, i)
        for line in comb:
            cg = 0
            cp = 0
            for j in line:
                cg += garr[j]
                cp += parr[j]
            #print line, cg, cp
            if cg > G:
                continue
            if cp >= P:
                cnt += 1
    return cnt              

import collections
def ans1(G, P, garr, parr):
    dp = collections.defaultdict(dict)
    
    dp[0] = {0:1} # num:{val:cnt}
    cnt = 0
    for i in xrange(len(garr)):
        #print dp
        #ndp = collections.defaultdict(dict)
        #ndp[0] = {0:1}
        keys = list(dp.keys())
        keys.sort()
        for key in keys[::-1]:
            nk = garr[i] + key
            if nk > G:
                continue
            val = parr[i]
            vkeys = list(dp[key].keys())
            for vkey in vkeys:
                nvk = val + vkey
                if nvk >= P:
                    cnt += dp[key][vkey]
                    nvk = P
                if dp[nk].has_key(nvk) == False:
                    dp[nk][nvk] = 0
                dp[nk][nvk] += dp[key][vkey]
        #dp = ndp
    #print dp
    return cnt % (10**9 + 7)

class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        return ans1(G, P, group, profit)
        
