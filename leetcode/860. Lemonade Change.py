import collections

def ans(bills):
    dic = collections.defaultdict(int)
    for b in bills:
        if b == 5:
            dic[b] += 1
        elif b == 10:
            if dic[5] == 0:
                return False
            dic[5] -= 1
            dic[10] += 1
        elif b == 20:
            if dic[10] >= 1 and dic[5] >= 1:
                dic[10] -= 1
                dic[5] -= 1
                dic[20] += 1
            elif dic[5] >= 3:
                dic[5] -= 3
                dic[20] += 1
            else:
                return False
    return True
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        return ans(bills)     
