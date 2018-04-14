import collections
def ans(routes, S, T):
    '''
    bfs method, converted routes to graph 
    '''
    dic = collections.defaultdict(list)
    for i in xrange(len(routes)):
        for bus in routes[i]:
            
    return 0
        
    

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        return ans(routes, S, T)   
    
    def test(self):
        cases = [
            ([[[1, 2, 7], [3, 6, 7]], 1, 6], 2),
        ]
        for i in xrange(len(cases)):
            c = cases[i]
            ret = self.numBusesToDestination(*c[0])
            print "case:%d: %d = %d"%(i + 1, ret, c[1]), (ret == c[1])

s = Solution()
s.test()
