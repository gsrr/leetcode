import collections

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = 0
        acnt = collections.Counter(answers)
        for key in acnt.keys():
            if key == 0:
                cnt += acnt[key]
            else:
                base = (key + 1)
                if acnt[key] % base == 0:
                    cnt += acnt[key]
                else:
                    cnt += ((acnt[key] / base + 1) * base)
                print cnt ,base
        return cnt
