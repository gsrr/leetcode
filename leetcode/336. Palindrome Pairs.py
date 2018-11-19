def is_palindrome(str1, str2):
    ss = str1 + str2
    return ss == ss[::-1]

def ans(words):
    ret = []
    for i in xrange(len(words)):
        for j in xrange(len(words)):
            if i == j:
                continue
            if is_palindrome(words[i], words[j]):
                ret.append([i, j])
    return ret

import collections
def ans1(words):
    cs = collections.defaultdict(list)
    for i in xrange(len(words)):
        cs[words[i]].append(i)
    
    ret = {}
    for key in cs.keys():
        # combine string in right-hand side.
        # abcd --> "", a, ba, cba, dcba
        for i in xrange(len(key) + 1):
            rstr = key[:i][::-1]
            if is_palindrome(key, rstr):
                for i in cs[key]:
                    for j in cs[rstr]:
                        if i == j:
                            continue
                        ret[(i, j)] = True
        
        # combine string in left-hand side.
        # "", d, dc, dcb, dcba <-- abcd
        
        for i in xrange(len(rstr) + 1):
            rstr = key[::-1][:i]
            if is_palindrome(rstr, key):
                for i in cs[rstr]:
                    for j in cs[key]:
                        if i == j:
                            continue
                        ret[(i, j)] = True
    return [list(key) for key in ret.keys()]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        return ans1(words)
