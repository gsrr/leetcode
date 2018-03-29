def seq_util(arr, tmp, ret):
    if len(tmp) > 1:
        ret.add(str(tmp))
    
    for i in xrange(len(arr)):
        if arr[i] >= tmp[-1]:
            tmp.append(arr[i])
            seq_util(arr[i + 1:], tmp, ret)
            tmp.pop()

def ans1(arr):
    '''
    Result : Accept
    Time complexity : O(n^2) --> n + (n - 1) + (n - 2) + ...
    Space complexity : O(2^n) --> possible result is 2^n
    '''
    ret = set([])
    for i in xrange(len(arr)):
        tmp = [arr[i]]
        seq_util(arr[i + 1:], tmp, ret)
    return [ eval(x) for x in list(ret)]

def ans2(arr):
    dp = set()
    for n in arr:
        for y in list(dp):
            if n >= y[-1]:
                dp.add(y + (n,))
        dp.add((n,))
    print dp
    return list(e for e in dp if len(e) > 1)

def ans3(arr):
    dp = {}
    for i in xrange(len(arr)):
        for key in dp.keys():
            if arr[i] >= key[-1]:
                dp[key + (arr[i],)] = True
        dp[(arr[i],)] = True
    return [ list(key) for key in dp.keys() if len(key) > 1 ]
    
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return ans3(nums)
        
