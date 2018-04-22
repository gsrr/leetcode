
def ans2(S, C):
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    carr = [-10000]
    for i in xrange(len(S)):
        if S[i] == C:
            carr.append(i)
    carr.append(20000)
    
    i = 0
    j = 0
    ret = []
    while i < len(S):
        if carr[j] < i:
            j += 1
        ret.append(min(i - carr[j - 1], carr[j] - i))
        i += 1
    return ret 

def ans1(S, C):
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    carr = []
    for i in xrange(len(S)):
        if S[i] == C:
            carr.append(i)
    
    i = 0
    j = 0
    ret = []
    while i < len(S):
        if j == len(carr):
            ret.append(i - carr[j - 1])
            i += 1
            continue
        if carr[j] >= i:
            if j == 0:
                ret.append(carr[j] - i)
            else:
                ret.append(min(carr[j] - i, i - carr[j - 1]))
            i += 1
        else:
            j += 1
       
    return ret 
            
            

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        return ans2(S, C)
        
