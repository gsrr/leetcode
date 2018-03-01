class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        i, j = 0, 0
        while i < len(strs[0]) and j < len(strs[-1]):
            if strs[0][i] == strs[-1][j]:
                i += 1
                j += 1
            else:
                break
        if i == 0:
            return ""
        return strs[0][0:i]
