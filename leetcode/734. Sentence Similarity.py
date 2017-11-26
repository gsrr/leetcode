import collections

def ans_1(words1, words2, pairs):
    '''
    dic structure
    
    Time Complexity : O(n)
    Result : Accept
    '''
    sim_dic = collections.defaultdict(dict)
    for i in xrange(len(pairs)):
        w1 = pairs[i][0]
        w2 = pairs[i][1]
        sim_dic[w1][w2] = True
        sim_dic[w1][w1] = True
        sim_dic[w2][w2] = True
        sim_dic[w2][w1] = True

    for i in xrange(len(words1)):
        w1 = words1[i]
        w2 = words2[i]
        if w1 == w2:
            continue
        if sim_dic.has_key(w1) == False:
            return False
        if sim_dic[w1].has_key(w2) == False:
            return False
    return True

def ans_2(words1, words2, pairs):
    '''
    Set structure
    
    Time Complexity : O(n)
    Result : Accept
    '''
    sp = set()
    for p in pairs:
        sp.add(tuple(p))
        p[0], p[1] = p[1], p[0]
        sp.add(tuple(p))
    
    for i in xrange(len(words1)):
        w1 = words1[i]
        w2 = words2[i]
        if w1 != w2 and (w1, w2) not in sp:
            return False
    return True

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        
        return ans_2(words1, words2, pairs)
