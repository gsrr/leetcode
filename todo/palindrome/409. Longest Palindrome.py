import collections

def ans(s):
    cs = collections.Counter(s)
    #rint cs
    cnt = 0
    for key in cs.keys():
        if cs[key] % 2 == 0:
            cnt += cs[key]
        else:
            cnt += cs[key] - 1
    gmax = 0
    for key in cs.keys():
        if cs[key] % 2 != 0:
            cnt += 1
            break
    return cnt
            
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        return ans(s)
        
