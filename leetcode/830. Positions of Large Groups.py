class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        i = 0
        j = 0
        cnt = 0
        while i < len(S) and j < len(S):
            if S[j] == S[i]:
                cnt += 1
                j += 1
            else:
                if cnt >= 3:
                    ret.append([i, j - 1])
                i = j
                cnt = 0
        if cnt >= 3:
            ret.append([i, j - 1])
        return ret 
        

s = Solution()
ex = "abbxxxxzzy"
print s.largeGroupPositions(ex)
ex = "abc"
print s.largeGroupPositions(ex)
ex = "abcdddeeeeaabbbcd"
print s.largeGroupPositions(ex)
