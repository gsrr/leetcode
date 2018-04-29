def ans(S):
    arr = [ list(w) for w in S.split()]
    #print arr
    cnt = 1
    for w in arr:
        if w[0] in ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']:
            w.append("ma")
        else:
            c = w.pop(0)
            w.append(c)
            w.append("ma")
        w.append("a" * cnt)
        cnt += 1
    return " ".join([ "".join(w) for w in arr ])

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return ans(S)
        
