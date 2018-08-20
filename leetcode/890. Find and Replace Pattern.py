def ans(words, pattern):
    ret = []
    for w in words:
        if len(w) != len(pattern):
            continue
        
        find = True
        dic = {}
        used = set([])
        for i in xrange(len(pattern)):
            if dic.has_key(pattern[i]) == False:
                if w[i] in used:
                    find = False
                    break
                dic[pattern[i]] = w[i]
                used.add(w[i])
            else:
                if dic[pattern[i]] != w[i]:
                    find = False
                    break
        if find:
            ret.append(w)
    return ret
    
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return ans(words, pattern)
        
