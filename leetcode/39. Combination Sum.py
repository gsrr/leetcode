import bisect


ret = []
def find_sub(cand, t, tarr):
    if t == 0:
        if len(tarr) != 0:
            ret.append(list(tarr))
        return
    
    idx = bisect.bisect_right(cand, t)
    if idx != 0:
        for i in xrange(idx - 1, -1, -1):
            if len(tarr) != 0 and tarr[-1] > cand[i]:
                continue
            tarr.append(cand[i])
            find_sub(cand, t - cand[i], tarr)
            tarr.pop()
    else:
        return
    

class Solution(object):
    def combinationSum(self, cand, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global ret
        ret = []
        cand.sort()
        arr = []
        find_sub(cand, target, arr)
        return ret
