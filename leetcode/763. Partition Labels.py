import collections

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        for i in xrange(len(S)):
            dic[S[i]].append(i)
        rs = []
        for key in dic.keys():
            rs.append(dic[key])
        rs.sort()
        #print rs
        ret = [rs[0]]
        for i in xrange(1, len(rs)):
            pre_s = ret[-1][0]
            pre_e = ret[-1][-1]
            post_s = rs[i][0]
            post_e = rs[i][-1]
            if post_s > pre_e:
                ret.append(rs[i])
            if post_e > pre_e:
                ret[-1][-1] = post_e
        #print ret
        return [x[-1] - x[0] + 1 for x in ret]
