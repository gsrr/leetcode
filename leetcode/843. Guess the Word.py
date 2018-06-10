# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

def is_sim(w1, w2, cnt):
    same = 0
    for i in xrange(len(w1)):
        if w1[i] == w2[i]:
            same += 1
    return same == cnt

def ans(words, master):
    ret = -1
    cand = set(words)
    while ret != 6:
        ncand = set([])
        for w1 in cand:
            print w1
            #print cand[0], ret
            ret = master.guess(w1)
            for w2 in cand:
                if is_sim(w1, w2, ret):
                    ncand.add(w2)
            break
        cand = ncand
        
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        return ans(wordlist, master)
