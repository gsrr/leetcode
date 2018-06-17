class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
    
    
    def find(self, u):
        if self.parent[u] == -1:
            return u
        return self.find(self.parent[u])
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return 
        
        if pu <= pv:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            
    def count(self):
        cnt = 0
        for i in xrange(len(self.parent)):
            if self.parent[i] == -1:
                cnt += 1
        return cnt
    
def catch_util(target, p1, s1, p2, s2):
    '''
    cnt = 1
    while p1 <= target and p2 <= target and p2 < p1:
        p2 += s2
        p1 += s1
    if p1 > target or p2 > target:
        return False
    return p2 >= p1
    '''
    d1 = target - p1
    d2 = target - p2
    t1 = d1 / float(s1)
    t2 = d2 / float(s2)
    return t2 <= t1
    

def is_catch(target, p1, s1, p2, s2):
    if p1 == p2:
        return True
    if s1 < s2:
        if p1 < p2:
            return False
        else:
            return catch_util(target, p1, s1, p2, s2)
    else:
        if p2 < p1:
            return False
        else:
            return catch_util(target, p2, s2, p1, s1)
    
def ans1(target, pos, speed):
    n = len(pos)
    ufs = UFS(n)
    for i in xrange(n):
        for j in xrange(i + 1, n):
            #print i, j
            if is_catch(target, pos[i], speed[i], pos[j], speed[j]):
                ufs.union(i, j)
    return ufs.count()

def ans(target, pos, speed):
    arr = []
    for i in xrange(len(pos)):
        arr.append([pos[i], speed[i]])
    arr.sort()
    print arr
    cnt = len(pos)
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            if is_catch(target, arr[i][0], arr[i][1], arr[j][0], arr[j][1]):
                cnt -= 1
                break
    return cnt

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        return ans(target, position, speed)        
