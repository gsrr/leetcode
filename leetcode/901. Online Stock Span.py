class StockSpanner(object):

    def __init__(self):
        self.pre = []
        self.pos = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # ans2
        cnt = 1
        i = len(self.pre) - 1
        while i > -1:
            if price >= self.pre[i]:
                cnt += self.pos[i]
                i -= self.pos[i]
            else:
                break
                
        self.pre.append(price)    
        self.pos.append(cnt)
        return cnt
    
        # ans1
        '''
        self.pre.append(price)
        cnt = 0
        for i in xrange(len(self.pre) - 1, -1, -1):
            if self.pre[i] > price:
                break
            cnt += 1
        return cnt
        '''
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
