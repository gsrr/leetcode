
def is_pa(s):
    for i in xrange(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

ret = []

def recur_util(s, path):
    if len(s) == 0:
        ret.append(list(path))
        return
    
    for i in xrange(len(s)):
        if is_pa(s[:i + 1]):
            path.append(s[:i + 1])
            recur_util(s[i + 1:], path)
            path.pop()
            
def ans(s):
    global ret
    ret = []
    path = []
    for i in xrange(len(s)):
        if is_pa(s[:i + 1]):
            path.append(s[:i + 1])
            recur_util(s[i + 1:], path)
            path.pop()
    return ret
            
def ans1(s):
    ret = []
    for i in xrange(len(s)):
        if is_pa(s[:i + 1]):
            tmp = s[: i + 1]
            if len(tmp) == len(s):
                ret.append([tmp])
            else:
                child = ans1(s[i + 1:])
                for c in child:
                    #fs = tmp + "".join(c)
                    #if len(fs) == len(s):
                    tmps = [tmp]
                    for cc in c:
                        tmps.append(cc)
                    ret.append(tmps)
    return ret
    
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return ans1(s)
        
