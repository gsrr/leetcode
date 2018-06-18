class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.arr = []

    def seat(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            self.arr.append(0)
            return 0
        
        index = 0
        gdist = -1
        if self.arr[0] != 0:
            gdist = self.arr[0] - 0 - 1
        
        for i in xrange(1, len(self.arr)):
            dist = self.arr[i] - self.arr[i - 1] - 1
            dist = (dist + 1) / 2 -1
            if dist > gdist:
                gdist = dist
                index = (self.arr[i] + self.arr[i - 1]) / 2
        
        if self.arr[-1] != self.n - 1:
            dist = self.n - 1 - self.arr[-1] - 1
            if dist > gdist:
                gdist = dist
                index = self.n - 1
        self.arr.append(index)
        self.arr.sort()
        return index
            
        
    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        for i in xrange(len(self.arr)):
            if self.arr[i] == p:
                self.arr.pop(i)
                break


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
