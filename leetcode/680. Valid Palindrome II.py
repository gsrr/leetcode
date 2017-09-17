class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = True
        end = True
        cnt = 1
        si = 0
        ei = len(s) - 1
        while si < len(s) / 2:
            if s[si] == s[ei]:
                si += 1
                ei -= 1
            else:
                cnt -= 1
                break
        if cnt == 1:
            return True
        firstr = s[si + 1: ei + 1]
        secstr = s[si : ei]
        
        for i in xrange(len(firstr) / 2):
            if firstr[i] != firstr[len(firstr) - 1 - i]:
                start = False
                break
        
        for i in xrange(len(secstr) / 2):
            if secstr[i] != secstr[len(secstr) - 1 - i]:
                end = False
                break
        
        if start == True or end == True:
            return True
        return False
