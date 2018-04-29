
def cond1(B, A):
    if B <= 0.5 * A + 7:
        return True
    return False

def cond2(B, A):
    if B > A:
        return True
    return False

def cond3(B, A):
    if B > 100 and A < 100:
        return True
    return False
        
def ans1(ages):
    '''
    Result : Time limit exceed
    '''
    ages.sort()
    cnt = 0
    for i in xrange(len(ages)):
        for j in xrange(len(ages)):
            if i == j:
                continue
            if cond1(ages[i], ages[j]) == True:
                continue
            if cond2(ages[i], ages[j]) == True:
                continue
            if cond3(ages[i], ages[j]) == True:
                continue
            cnt += 1
    return cnt

import collections
def ans(ages):
    cages = collections.Counter(ages)
    #print cages
    keys = cages.keys()
    keys.sort()
    cnt = 0
    for i in xrange(len(keys)):
        for j in xrange(i, len(keys)):
            if i == j and cages[keys[i]] == 1:
                continue
            if cond1(keys[i], keys[j]) == True:
                continue
            #if cond2(keys[i], keys[j]) == True:
                #continue
            if cond3(keys[i], keys[j]) == True:
                continue
            
            if i == j:
                cnt += (cages[keys[i]] * (cages[keys[i]] - 1))
            else:
                cnt += (cages[keys[i]] * cages[keys[j]])
    return cnt
    
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        return ans(ages)
