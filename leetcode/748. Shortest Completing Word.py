def is_valid(w, dic):
    dic_w = collections.defaultdict(int)
    for c in w:
        if c.isalpha():
            dic_w[c.lower()] += 1
            
    for c in dic.keys():
        if dic_w.has_key(c) == False:
            return False
        if dic_w[c] < dic[c]:
            return False
    return True

def ans(base, words):
    dic = collections.defaultdict(int)
    for i in xrange(len(base)):
        c = base[i]
        if c.isalpha():
            dic[c.lower()] += 1
    
    gw = ""
    glen = 0x7fffffff
    for w in words:
        if is_valid(w, dic):
            if len(w) < glen:
                gw = w
                glen = len(w)
    return gw

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        return ans(licensePlate, words)
