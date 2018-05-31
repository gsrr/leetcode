def is_fib(v1, v2, arr, ret):
    if len(arr) == 0:
        return True
    
    for i in xrange(1, len(arr) + 1):
        v3 = int(arr[0:i])
        ret.append(v3)
        if (v1 + v2) != v3:
            ret.pop()
            continue
        if is_fib(v2, v3, arr[i:], ret):
            return True
        ret.pop()
    return False

def ans(S):
    ret = []
    for i in xrange(1, len(S)):
        v1 = int(S[0:i])
        for k in xrange(0, i):
            if S[k] == '0':
                if v1 == 0:
                    break
            else:
                break
        ret.append(v1)
        for j in xrange(i + 1, len(S)):
            v2 = int(S[i:j])
            ret.append(v2)
            if is_fib(v1, v2, S[j:], ret):
                return ret
                return True
            ret.pop()
        ret.pop()
    return ret
    return False

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        return ans(S)
