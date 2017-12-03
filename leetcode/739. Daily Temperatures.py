def ans_4(ts):
    '''
    1. Each temperature will be an integer in the range [30, 100].
    2. best is array
    
    Time Complexity : O(70 * n)
    Result : Accept
    '''
    ret = [0x7fffffff] * len(ts)
    best = [-1] * 101
    for i in xrange(len(ts) - 1, -1, -1):
        for j in xrange(ts[i] + 1, 101):
            if j > ts[i] and best[j] > 0:
                ret[i] = min(best[j] - i, ret[i])
        if ret[i] == 0x7fffffff:
            ret[i] = 0
        best[ts[i]] = i
    return ret

def ans_3(ts):
    '''
    1. Each temperature will be an integer in the range [30, 100].
    2. best is dictionary (best.get(j) is slower than best[j])
    
    Time Complexity : O(70 * n)
    Result : Accept
    '''
    ret = [0x7fffffff] * len(ts)
    best = {}
    for i in xrange(len(ts) - 1, -1, -1):
        for j in xrange(ts[i] + 1, 101):
            if j > ts[i] and best.get(j) != None:
                if best[j] - i < ret[i]:
                    ret[i] = best[j] - i
        if ret[i] == 0x7fffffff:
            ret[i] = 0
        best[ts[i]] = i
    return ret

def ans_2(ts):
    '''
    Time Complexity : O(n)
    Result : Accept
    '''    
    ret = [0] * len(ts)
    stack = []
    for i in xrange(len(ts)):
        if len(stack) != 0:
            val = ts[i]
            while len(stack) != 0:
                sval, si = stack.pop()
                if val > sval:
                    ret[si] = i - si
                else:
                    stack.append([sval, si])
                    break
        stack.append([ts[i], i])
    return ret
    
def ans_1(ts):
    '''
    Time Complexity : O(n^2)
    Result : Time Limit Exceeded
    '''
    ret = []
    for i in xrange(len(ts)):
        j = i + 1
        find = False
        while j < len(ts): 
            if ts[j] > ts[i]:
                find = True
                break
            j += 1
        if find == False:
            ret.append(0)
        else:
            ret.append(j - i)
    return ret

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        return ans_2(temperatures)
        
