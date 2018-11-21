
def get_diff(v1, v2):
    return abs(v1-v2)

def even(half, n):
    cs = n[0:half]
    pres = str(int(cs) - 1)
    posts = str(int(cs) + 1)
    
    nval = int(n)
    cval = int(cs[:] + cs[::-1])
    postval =  int(posts[:] + posts[::-1])
    if len(posts) > len(cs):
        postval =  int(posts[:] + posts[::-1][1:])
    preval = int(pres[:] + pres[::-1])
    nineval = int("9" * (len(n) - 1) )
    
    if cval == nval:
        darr = [[get_diff(postval, nval), postval], [get_diff(preval, nval), preval], [get_diff(nineval, nval), nineval]]
    else:
        darr = [[get_diff(postval, nval), postval], [get_diff(preval, nval), preval], [get_diff(nineval, nval), nineval], [get_diff(cval, nval), cval]]
    
    darr.sort()
    #print darr
    return str(darr[0][1])

def odd(half, n):
    cs = n[0:half + 1]
    pres = str(int(cs) - 1)
    posts = str(int(cs) + 1)
    
    nval = int(n)
    cval = int(cs[:] + cs[::-1][1:])
    postval =  int(posts[:] + posts[::-1][1:])
    if len(posts) > len(cs):
        postval =  int(posts[:-1] + posts[:-1][::-1])
    preval = int(pres[:] + pres[::-1][1:])
    nineval = int("9" * (len(n) - 1) )
    
    if cval == nval:
        darr = [[get_diff(postval, nval), postval], [get_diff(preval, nval), preval], [get_diff(nineval, nval), nineval]]
    else:
        darr = [[get_diff(postval, nval), postval], [get_diff(preval, nval), preval], [get_diff(nineval, nval), nineval], [get_diff(cval, nval), cval]]
    
    darr.sort()
    #print darr
    return str(darr[0][1])
        
def ans(n):
    ln = len(n)
    if ln == 1:
        return str(int(n) - 1)
    half = ln / 2
    if ln % 2 == 0:
        return even(half, n)
    else:
        return odd(half, n)

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        return ans(n)
        
