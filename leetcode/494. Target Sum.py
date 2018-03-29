
import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values


def ans2(nums, S):
    '''
    Result : accept
    Time complexity : O(n * S)
    Space complexity : O(S)
    '''
    if len(nums) == 0:
        return 0
    
    dp = {0 : 1}
    for i in xrange(len(nums)):
        ndp = collections.defaultdict(int)
        for key in dp.keys():
            ndp[key + nums[i]] += dp[key]
            ndp[key - nums[i]] += dp[key]
        dp = ndp
    return dp[S]

def ans1(nums, S):
    '''
    Recursive method
    Time Complexity : O(2^n)
    Space Complexity : O(n), due to stack of function all
    Result : Time Limit Exceeded 
    '''
    
    if len(nums) == 0:
        if S == 0:
            return 1
        else:
            return 0
    cnt = 0
    for sign in [1, -1]:
        val = nums.pop()
        cnt += ans1(nums, S - (val * sign))
        nums.append(val)
    return cnt

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return ans2(nums, S)
        
