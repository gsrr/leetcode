
def ans(S, indexes, sources, targets):
    ret = [0] * len(S)
    for i in xrange(len(indexes)):
        sub1 = sources[i]
        sub2 = S[indexes[i] : indexes[i] + len(sub1)]
        if sub1 == sub2:
            ret[indexes[i]] = targets[i]    
            for j in xrange(indexes[i] + 1, indexes[i] + len(sub1)):
                ret[j] = ""
    for i in xrange(len(ret)):
        if ret[i] == 0:
            ret[i] = S[i]
    return "".join(ret)

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        return ans(S, indexes, sources, targets)        

S = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
print ans(S, indexes, sources, targets)

S = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print ans(S, indexes, sources, targets)
