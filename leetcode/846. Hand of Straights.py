import collections

def ans1(arr, w):
    n = len(arr)
    if n % w != 0:
        return False
    
    carr = [ list(x) for x in collections.Counter(arr).items()]
    carr.sort()
    while len(carr) >= w:
        n = len(carr)
        pre = carr[-1][0]
        #print carr, pre
        carr[-1][1] -= 1
        if carr[-1][1] == 0:
            carr.pop()
        cnt = w - 1
        n -= 1
        for i in xrange(n- 1, -1, -1):
            if cnt == 0:
                break
            if carr[i][0] == pre - 1:
                pre = carr[i][0]
                cnt -= 1
                carr[i][1] -= 1
                if carr[i][1] == 0:
                    carr.pop(i)
            else:
                return False

    if len(carr) != 0:
        return False
    return True

def ans(arr, w):
    n = len(arr)
    if n % w != 0:
        return False
    
    carr = [ list(x) for x in collections.Counter(arr).items()]
    carr.sort()
    while len(carr) >= w:
        pre = carr[-1][0] + 1
        cnt = w
        i = len(carr) - 1
        while cnt > 0:
            if carr[i][0] == pre - 1:
                pre = carr[i][0]
                carr[i][1] -= 1
                if carr[i][1] == 0:
                    carr.pop(i)
            else:
                return False
            cnt -= 1
            i -= 1
    
    if len(carr) != 0:
        return False
    return True

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        return ans(hand, W)
        
