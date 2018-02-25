
import string

def compare(base_dic):
        def wrap_func(a, b):
            if base_dic[a] >= base_dic[b]:
                return 1
            else:
                return -1
        return wrap_func

def ans1(ss, ts):
    letters = string.ascii_lowercase
    base_dic = {}
    for i in xrange(len(letters)):
        base_dic[letters[i]] = i
    print base_dic
    ts_set = set(ts)
    for i in xrange(len(ss) - 1, -1, -1):
        tmp = 27
        find = False
        for j in xrange(i + 1, len(ss)):
            if ss[j] in ts_set and ss[i] in ts_set:
                if base_dic[ss[i]] < base_dic[ss[j]]:
                    continue
                print ss[i], ss[j], base_dic[ss[i]], base_dic[ss[j]]
                tmp = min(tmp, base_dic[ss[j]])
                find = True
        if find:
            base_dic[ss[i]] = tmp - 0.1
    print base_dic
    lts = list(ts)
    return "".join(sorted(lts, cmp = compare(base_dic)))
    
    
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        return ans1(S, T)    
