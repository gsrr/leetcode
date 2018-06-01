
def is_valid(val):
    for i in xrange(len(val)):
        if val[i] == '0':
            if len(val) == 1:
                return True
            else:
                return False
        else:
            return True

def is_fib(v1, v2, arr, ret):
    if v1 > 0x7fffffff or v2 > 0x7fffffff:
        return False
    if len(arr) == 0:
        return True
    
    for i in xrange(1, len(arr) + 1):
        v3 = arr[0:i]
        if is_valid(v3) == False:
            continue
        v3 = int(v3)
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
        v1 = S[0:i]
        if is_valid(v1) == False:
            continue
        v1 = int(v1)
        ret.append(v1)
        for j in xrange(i + 1, len(S)):
            v2 = S[i:j]
            if is_valid(v2) == False:
                continue
            v2 = int(v2)
            ret.append(v2)
            if is_fib(v1, v2, S[j:], ret):
                return ret
            ret.pop()
        ret.pop()
    return ret

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        return ans(S)

S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
print ans(S)

S = "417420815174208193484163452262453871040871393665402264706273658371675923077949581449611550452755"
print ans(S)
