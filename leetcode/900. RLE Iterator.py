class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        '''
        self.arr = []
        for i in xrange(0, len(A), 2):
            num = A[i]
            val = A[i + 1]
            for j in xrange(num):
                self.arr.append(val)
        self.index = -1
        '''
        self.arr = A
        self.index = 0
        self.pos = 0
        
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        # ans1
        self.index += n
        if self.index >= len(self.arr):
            return -1
        return self.arr[self.index]
        '''
        #ans2
        self.index += n
        tmp = self.index
        for i in xrange(self.pos, len(self.arr), 2):
            num = self.arr[i]
            val = self.arr[i + 1]
            tmp -= num
            if tmp <= 0:
                self.pos = i
                self.index = (tmp + num)
                return val
        self.pos = len(self.arr)
        return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
