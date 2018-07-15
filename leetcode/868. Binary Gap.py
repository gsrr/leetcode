def ans(n):
    tn = n
    v1 = (0, 0)
    v2 = (0, 0)
    cnt = 0
    gdist = 0
    while tn != 0:
        cnt += 1
        val = tn % 2
        tn = tn / 2
        if val == 0:
            continue
        if v1[0] == 0:
            v1 = (1, cnt)
        else:
            v2 = (1, cnt)
            gdist = max(v2[1] - v1[1], gdist)
            v1 = v2
    return gdist
            
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        return ans(N)
        
