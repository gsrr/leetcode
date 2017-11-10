def ans_1(bits):    
    '''
    Travse all array
    
    Time Complexity : O(n)
    Result : Accept
    '''
    ret = False
    cnt = 0 
    while cnt < len(bits):
        if bits[cnt] == 1:
            cnt += 2
            ret = False
        elif bits[cnt] == 0:
            ret = True
            cnt += 1

    return ret
    
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        return ans_2(bits)
