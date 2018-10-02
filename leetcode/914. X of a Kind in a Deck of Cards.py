import collections

def ans(arr):
    carr = collections.Counter(arr)
    for key in carr.keys():
        if carr[key] < 2:
            return False
    
    #print carr
    val = carr[arr[0]]
    v = 1
    while v * v <= val:
        if val % v == 0:
            #print val, v
            v1 = v
            v2 = val / v1
            for vt in [v1, v2]:
                find = True
                if vt == 1:
                    continue
                for key in carr.keys():
                    if carr[key] % vt != 0:
                        find = False
                        break
                if find:
                    return True
        v += 1
    return False

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        return ans(deck)
