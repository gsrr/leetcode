import collections

def get_maxcnt(dic):
    maxcnt = 0
    for key in dic.keys():
        if dic[key] > maxcnt:
            maxcnt = dic[key]
    return maxcnt

class Solution(object):
    def characterReplacement(self, ss, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(ss) == 0:
            return 0
        dic = collections.defaultdict(int)
        s = 0
        e = 0
        max_val = 0
        dic[ss[e]] += 1
        while e < len(ss):
            maxcnt = get_maxcnt(dic)
            tval = maxcnt + k
            wins = e - s + 1
            if wins <= tval:
                max_val = max(max_val, tval)
                e += 1
                if e == len(ss):
                    break
                dic[ss[e]] += 1
            elif wins > tval:
                dic[ss[s]] -= 1
                s += 1
        return min(max_val, len(ss))
                
        
