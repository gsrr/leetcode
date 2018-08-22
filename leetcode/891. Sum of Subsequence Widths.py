def ans1(arr):
    '''
    Result : Time Exceed
    Time Complexity : O(n^2)
    '''
    arr.sort()
    sval = 0
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            num = pow(2, j - i - 1)
            sval += (arr[j] - arr[i]) * num
    return sval % (10**9 + 7)

def ans(arr):
    '''
    a1 + 2(a1 + a2) + 4 (a1 + a2 + a3) + ...
         a2 + 2 (a2 + a3) + ...
    '''
    arr.sort()
    diffArr = []
    for i in xrange(1, len(arr)):
        diffArr.append(arr[i] - arr[i - 1])
    
    sval = 0
    ans = 0
    num = 0
    for i in xrange(len(diffArr)):
        num = num * 2 + 1
        sval = sval * 2 + num * diffArr[i]
        ans += sval
        ans = ans % (10**9 + 7)
    return ans
    
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
        
