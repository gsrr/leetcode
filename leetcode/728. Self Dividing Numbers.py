def find(val):
    tmp = val
    while tmp != 0:
        d = tmp % 10
        if d == 0:
            return False
        if val % d != 0:
            return False
        tmp = tmp / 10
    return True

def ans_1(left, right):
    '''
    Time Complexity : O(n)
    
    '''
    ret = []
    for val in xrange(left, right + 1, 1):
        if find(val) == True:
            ret.append(val)
    return ret

def find_2(val):
    sval = str(val)
    for c in sval:
        d = ord(c) - 48
        if d == 0:
            return False
        if val % d != 0:
            return False
    return True

def ans_2(left, right):
    ret = []
    for val in xrange(left, right + 1, 1):
        if find_2(val) == True:
            ret.append(val)
    return ret

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return ans_2(left, right)
