class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[-1] = (1, 1)
        for i in xrange(len(nums) - 2, -1, -1):
            mlen = 1
            cnt = 1
            for j in xrange(i + 1, len(nums)):
                if nums[j] - nums[i] > 0:
                    if dp[j][0] + 1 > mlen:
                        mlen = dp[j][0] + 1
                        cnt = dp[j][1]
                    elif dp[j][0] + 1 == mlen:
                        cnt += dp[j][1]
                    else:
                        pass 
                    
            dp[i] = (mlen, cnt)
        
        print dp
        mval = dp[0][0]
        mcnt = dp[0][1]
        for i in xrange(1, len(dp)):
            if dp[i][0] > mval:
                mval = dp[i][0]
                mcnt = dp[i][1]
            elif dp[i][0] == mval:
                mcnt += dp[i][1]
        return mcnt
                 
'''
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
'''
