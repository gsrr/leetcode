
def judge(s):
    #print "judge:", s
    if s == s[::-1]:
        return True 
    return False


def recur_util(ls):
    if ls[0] == ls[-1]:
        if recur_util(ls[1:-1]):
            return True

    if judge(ls[1:]):
        return True
    if judge(ls[:-1]):
        return True
    return False

def ans(s):
    ls = list(s)
    '''
    從外面開始比, 只會有三種case:
    1. 兩個都不刪除.
    2. 刪除前面.
    3. 刪除後面.
    '''
    if ls[0] == ls[-1]:
        if recur_util(ls[1:-1]):
            return True

    if judge(ls[1:]):
        return True
    if judge(ls[:-1]):
        return True
        
    return False    

def ans1(s):
    si = 0
    ei = len(s) - 1
    mid = len(s) // 2
    while si < mid:
        if judge(s[si + 1:ei + 1]):
            return True
        if judge(s[si:ei]):
            return True
        if s[si] == s[ei]:
            si += 1
            ei -= 1
        else:
            break
    return si == mid

def ans2(ss, s, e, quota):
    if s >= e:
        return True
    if ss[s] == ss[e - 1]:
        if ans2(ss, s + 1, e - 1, quota):
            return True
    if quota == 0:
        return False

    if ans2(ss, s + 1, e, 0):
        return True
    if ans2(ss, s, e - 1, 0):
        return True 
    return False    


def ans3(ss, s, e):
    if s >= e:
        return True
    if ss[s] == ss[e - 1]:
        return ans3(ss, s + 1, e - 1)    

    if judge(ss[s+1:e]):
        return True
    if judge(ss[s:e-1]):
        return True 
    return False  

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        ls = list(s)
        return ans3(ls, 0, len(ls))
