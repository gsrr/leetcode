import collections

def ans(A, B):
    wa = A.strip().split()
    wb = B.strip().split()
    
    dica = collections.Counter(wa)
    dicb = collections.Counter(wb)
    
    print dica, dicb
    ret = []
    for key in dica.keys():
        #print key
        if dica[key] != 1:
            #print "%s:key > 1"%key
            continue
        if dicb[key] != 0:
            #print "%s:key != 0"%key
            continue
        ret.append(key)
        
    for key in dicb.keys():
        if dicb[key] != 1:
            continue
        if dica[key] != 0:
            continue
        ret.append(key)
    return ret

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        return ans(A, B)
