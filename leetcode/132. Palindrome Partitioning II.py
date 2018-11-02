gcache = {}
paliarr = []

def is_palindrome2(ls, i, j):
    s = ls[i:j+1]
    return s == s[::-1]

def is_palindrome(ls, i, j):
    global paliarr
    return paliarr[i][j]

def recur_util(ls, i):
    if is_palindrome(ls, i, len(ls) - 1):
        return 0
    key = ls[i:]
    if gcache.has_key(key):
        return gcache[key]
    
    lmin = len(ls) - 1
    for j in xrange(i + 1, len(ls) + 1):
        if is_palindrome(ls, i, j - 1):
            cnt = 1 + recur_util(ls, j)
            #print ls[i:j], cnt
            lmin = min(lmin, cnt)
    gcache[key] = lmin
    return lmin

def ans(s):
    global gcache, paliarr
    gcache = {}
    paliarr = [ [True] * len(s) for _ in xrange(len(s)) ]

    for i in xrange(1, len(s) + 1):
        for j in xrange(len(s)):
            start = j
            end = j + i - 1
            if end >= len(s):
                continue
            if s[start] == s[end]:
                if start + 1 > end - 1:
                    paliarr[start][end] = True
                else:
                    paliarr[start][end] = paliarr[start + 1][end - 1]    
            else:
                paliarr[start][end] = False
    
    #print paliarr
    ls = s
    if is_palindrome(ls, 0, len(ls) - 1):
        return 0
    
    
    gmin = len(ls) - 1
    for i in xrange(1, len(ls) + 1):
        if is_palindrome(ls, 0, i - 1):
            cnt = 1 + recur_util(ls, i)
            #print ls[0:i], cnt
            gmin = min(gmin, cnt)
    return gmin

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return ans(s)
        
