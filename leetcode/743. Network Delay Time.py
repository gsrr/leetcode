import collections
import heapq

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for s, t, c in times:
            dic[s].append((c, t))
        
        ret = 0
        hist = {}
        q = []
        heapq.heappush(q, (0, K))
        while len(q) != 0:
            cost, node = heapq.heappop(q)
            if hist.has_key(node):
                continue
            ret = cost
            hist[node] = True
            for nnode in dic[node]:
                heapq.heappush(q, (nnode[0] + cost, nnode[1]))
        if len(hist.keys()) != N:
            return -1
        return ret
