def ans(s):
    s = s.lower()
    ss = []
    for i in xrange(len(s)):
        if s[i].isalnum():
            ss.append(s[i])
    if len(ss) == 0:
        return True
    
    return ss == ss[::-1]

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return ans(s)
        
