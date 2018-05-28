def lowbit(x):
    '''
    low-bit means the value of last 1.
    The position will be x & (-x) due to 2's complement.
    (2's complement is inverse(x) + 1 --> 100 is (011 + 1) = 100 --> will be last bit of 1)
    '''
    return x & (-x)

# The bit node is the summation of previous nodes.

class BIT:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (len(arr) + 1)
        for i in xrange(len(arr)):
            self.update(i, arr[i])

    def sum(self, i):
        i += 1
        s = 0 
        while i > 0:
            s += self.tree[i]
            i -= (i & (-i))      
        return s        

    def update(self, i, v):
        '''
        update bit node
        '''
        i += 1 # 0 is dummy node
        while i <= self.n:
            self.tree[i] += v
            i += (i & (-i))

'''
Sum of elements in arr[0..5] is 12
Sum of elements in arr[0..5] after update is 18
'''

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit = BIT(freq)
print bit.tree
print("Sum of elements in arr[0..5] is " + str(bit.sum(5)))
freq[3] += 6
bit.update(3, 6)
print("Sum of elements in arr[0..5] is " + str(bit.sum(5)))
